import subprocess
import fpga
import pathlib
import os
import time 

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


class VlibDriver():
	def __init__(self,modelsim_path, target_path = pathlib.Path.cwd(), lib_name = "work"):
		self.process = subprocess.Popen([modelsim_path  / 'vlib',"-target" , target_path / lib_name],
			universal_newlines=True,
			stdout=subprocess.PIPE)
		self.outs, self.errs = self.process.communicate()
		return


class VmapDriver():
	def __init__(self, modelsim_path, target_path = pathlib.Path.cwd(), lib_name = "work"):
		self.process = subprocess.Popen([modelsim_path / "vmap", lib_name,target_path/lib_name],
			universal_newlines=True,
			stdout=subprocess.PIPE)
		self.outs, self.errs = self.process.communicate()


class VlogDriver():
	def __init__(self, modelsim_path, target_path = pathlib.Path.cwd(),verilog_files = "**.v", lib_name = "work"):
		self.process = subprocess.Popen([modelsim_path / "vlog","-nocreatelib","+incdir+"+str(target_path),"-work",target_path/lib_name ,target_path/verilog_files],
			universal_newlines=True,
			stdout=subprocess.PIPE)
		self.outs, self.errs = self.process.communicate()


class VsimDriver():
	def __init__(self, modelsim_path, top_level_entity,target_path = pathlib.Path.cwd(), time_resolution = "1ms"):
		self.process = subprocess.Popen([modelsim_path / "vsim", "-t", time_resolution, "-c", "-wlfslim", "1","-Ldir", target_path / "work", "work."+top_level_entity],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			shell=False,
			universal_newlines=True)	
		self.process.stdin.flush()
		print(modelsim_read(self.process))
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
		# self.process.stdin.write("quit -sim \n")
		self.process.stdin.write("exit \n")	
		self.process.stdin.flush()
		

class VsimController():
	def __init__(self, fpga,config):
		self.fpga = fpga
		self.config = config
		self.vsim = VsimDriver(config["modelsim_path"], config["lib_top_level_entity"], target_path = config["target_path"])


	def group_force(self):
		for (name, port) in self.fpga.get_all(): 
			if port.direction == "input":
				self.vsim.force(self.config["lib_top_level_entity"], port.name, port.get_value_lsb() )
	

	def group_examine(self):
		for (name, port) in self.fpga.get_all(): 
			if port.direction == "output":
				data = self.vsim.examine(port.name)
				if ("Error" not in data):
					blocks = data.split()
					port.set_value_lsb(blocks[3])


	def quitsim(self):
		self.vsim.quitsim()


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


