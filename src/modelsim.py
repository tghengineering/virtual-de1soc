import subprocess
import fpga
import pathlib
import config
import os

def modelsim_write(proc,command):
	proc.stdin.write(command)	
	proc.stdin.flush()


def modelsim_read(proc):
	dat = ""
	dat_out = ""
	while (True):
		dat = proc.stdout.read(1)
		if (not dat) or (dat == ">"):
			break
		dat_out=dat_out+dat
	return dat_out

def proc_kill(proc):
	os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

# TODO RE ADD TARGET LOACTION
class VlibDriver():
	def __init__(self,modelsim_path, target_path = "", lib_name = "work"):
#		self.process = subprocess.Popen([modelsim_path  / 'vlib',"-target ", lib_name],
		self.process = subprocess.Popen([modelsim_path  / 'vlib', lib_name],
			universal_newlines=True,
			stdout=subprocess.PIPE)

class VmapDriver():
	def __init__(self, modelsim_path, target_path = "", lib_name = "work"):
		self.process = subprocess.Popen([modelsim_path / "vmap", "work ",lib_name],
			universal_newlines=True,
			stdout=subprocess.PIPE)

class VlogDriver():
	def __init__(self, modelsim_path, target_path = "" ,verilog_files = "**.v", lib_name = "work"):
#		self.process = subprocess.Popen([modelsim_path / "vlog","-work ",lib_name, verilog_files],
		self.process = subprocess.Popen([modelsim_path / "vlog", verilog_files],
			universal_newlines=True,
			stdout=subprocess.PIPE)

class VsimDriver():
	def __init__(self, modelsim_path, top_level_entity,target_path = "", time_resolution = "1ms"):
#		self.process = subprocess.Popen([modelsim_path / "vsim", "-t", time_resolution, "-c", "-wlfslim", "1","-Ldir", target_path / "work", "work."+top_level_entity],
		self.process = subprocess.Popen([modelsim_path / "vsim", "-t", time_resolution, "-c", "-wlfslim", "1","work."+top_level_entity],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			shell=True,
			universal_newlines=True)	
		self.process.stdin.flush()
		(modelsim_read(self.process))
		self.process.stdin.write("transcript file \"\"\n")	

		self.process.stdin.flush()
		modelsim_read(self.process)

	def force(self, top_level_entity, port_name, port_value):
		self.process.stdin.write("force sim:/"+top_level_entity+"/"+port_name+" "+port_value+" \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)

	def examine(self, port_name):
		self.process.stdin.write("examine "+port_name+"  \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)
	
	def step(self):
		self.process.stdin.write("run 1 \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)
	
	def run(self, duration):
		self.process.stdin.write("run "+duration+ " \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)
	
	def restart(self):
		self.process.stdin.write("restart \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)

	def quitsim(self):
		self.process.stdin.write("quit -sim \n")	
		self.process.stdin.flush()
		return modelsim_read(self.process)


class BoardSimulator():
	def __init__(self, fpga,config):
		self.fpga = fpga
		self.config = config
		self.vlib = VlibDriver(config["modelsim_path"], target_path = config["lib_target_path"] )
		self.vmap = VmapDriver(config["modelsim_path"], target_path = config["lib_target_path"] )
		self.vlog = VlogDriver(config["modelsim_path"], target_path = config["lib_target_path"] )
		self.vsim = VsimDriver(config["modelsim_path"], config["lib_top_level_entity"], target_path = config["lib_target_path"])


	def group_force(self):
		for (name, port) in self.fpga.get_all(): 
			if port.direction == "input":
				self.vsim.force(self.config["lib_top_level_entity"], port.name, port.get_value_lsb() )
	

	def group_examine(self):
		for (name, port) in self.fpga.get_all(): 
			if port.direction == "output":
				data = self.vsim.examine(port.name)
				if ("Error" not in data):
					numbers = [ block for block in data.split() if block.isdigit() ]
					if (len(numbers) >= 1):
						port.set_value_lsb(numbers[0])


	def step(self):
		## Force Update the sim then step and examine
		self.group_force()
		self.vsim.step()
		self.group_examine()

	def run(self, duration):
		## Force Update the sim then run and examine
		self.group_force()
		self.vsim.run(duration)
		self.group_examine()


