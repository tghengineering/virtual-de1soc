import subprocess
import fpga
import config

def modelsim_write(proc,command):
	proc.stdin.write(command)	
	proc.stdin.flush()


def modelsim_read(proc):
	dat = ""
	dat_out = ""
	while (True):
		dat = proc.stdout.read(1)
		if not dat:
			break
		if (dat == ">"):
			break
		dat_out=dat_out+dat
	return dat_out.strip().split("\n")


class VlibDriver():
	def __init__(self,config):
		#self.config = config
		self.proc_vlib = subprocess.run(config.modelsim_path+"vlib work",
			stdin=subprocess.DEVNULL, 
			stdout=subprocess.DEVNULL, 
			stderr=subprocess.DEVNULL)

class VmapDriver():
	def __init__(self,config):
		#self.config = config
		self.proc_vlib = subprocess.run(config.modelsim_path+"vmap work work",
			stdin=subprocess.DEVNULL, 
			stdout=subprocess.DEVNULL, 
			stderr=subprocess.DEVNULL)

class VlogDriver():
	def __init__(self,config):
		#self.config = config
		self.proc_vlib = subprocess.run(config.modelsim_path+"vlog *.v",
			stdin=subprocess.DEVNULL, 
			stdout=subprocess.PIPE, 
			stderr=subprocess.DEVNULL)
		#print(self.proc_vlib.stdout)

class VsimDriver():
	def __init__(self):
		self.config = config
		self.fpga = fpga
		self.proc_vsim = subprocess.Popen([self.config.modelsim_path+"vsim", "-c", "-wlfslim", "1", "work."+"MyProject"],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.DEVNULL,
			shell=True,
			universal_newlines=True)
	
		self.proc_vsim.stdin.flush()
		self.proc_vsim.stdout.flush()

		modelsim_read(self.proc_vsim)

		self.proc_vsim.stdin.write("transcript file \"\"\n")	
		self.proc_vsim.stdin.flush()

		modelsim_read(self.proc_vsim)

	def force(self, port_name):
		self.proc_vsim.stdin.write("force sim:/"+self.config.top_level_entity+"/"+port_name+" "+self.fpga.__dict__[port_name].value_str()+" \n")	
		self.proc_vsim.stdin.flush()
		return modelsim_read(self.proc_vsim)

	def examine(self, port_name):
		self.proc_vsim.stdin.write("examine "+port_name+"  \n")	
		self.proc_vsim.stdin.flush()
		data = modelsim_read(self.proc_vsim)
		if not any("Error" in dat for dat in data):
			self.fpga.__dict__[port_name].value_set(data[1])
		return data
	
	def step(self):
		self.proc_vsim.stdin.write("run 1 \n")	
		self.proc_vsim.stdin.flush()
		return modelsim_read(self.proc_vsim)
	
	def run(self, duration):
		self.proc_vsim.stdin.write("run "+duration+ " \n")	
		self.proc_vsim.stdin.flush()
		return modelsim_read(self.proc_vsim)
	
	def restart(self):
		self.proc_vsim.stdin.write("restart \n")	
		self.proc_vsim.stdin.flush()
		return modelsim_read(self.proc_vsim)

	def quitsim(self):
		self.proc_vsim.stdin.write("quit -sim \n")	
		self.proc_vsim.stdin.flush()
		return modelsim_read(self.proc_vsim)

	def group_force(self):
		for (name, port) in self.fpga.__dict__.items(): 
			if port.direction == "input":
				self.force(name)

	def group_examine(self):
		for (name, port) in self.fpga.__dict__.items(): 
			if port.direction == "output":
				self.examine(name)

	class Simulator():
		def __init__(self, fpga,config):
			self.vlib = VlibDriver(config)
			#self.vmap = VmapDriver
			#self.vlog = VlogDriver
			#self.vsim = VsimDriver
