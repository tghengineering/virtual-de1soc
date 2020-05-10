import os
import pathlib

class Config():
	def __init__(self):

		#TODO add json config 

		self.vsim_step = True

		
		self.vsim_duration = "10ns"
		self.lib_target_path = pathlib.Path.cwd()
		self.lib_name = "work"
		self.lib_top_level_entity = "MyProject"

		#Windows
		if os.name == 'nt': 
			self.modelsim_path = pathlib.Path("C://intelFPGA_lite//18.1//modelsim_ase//win32aloem//")
		# for mac and linux(here, os.name is 'posix') 
		else:  
			self.modelsim_path = pathlib.Path("/home/ff/intelFPGA_lite//18.1//modelsim_ase//linuxaloem//")

		self.time_delay = 0.2
		self.SW_key = ["0","9","8","7","6","5","4","3","2","1"]
		self.KEY_key = ["p","o","i","u"]
