import os

class Config():
	def __init__(self):
		self.modelsim_path = "C:\\intelFPGA_lite\\18.1\\modelsim_ase\\win32aloem\\"
		
		self.vsim_duration = "10ns"
		self.vsim_step = True
		self.lib_target_path = ""
		self.lib_name = "work"
		self.lib_top_level_entity = "MyProject"
		# for windows 
		#if os.name == 'nt': 
		#	self.modelsim_path = "C:\\intelFPGA_lite\\18.1\\modelsim_ase\\win32aloem\\"
		# for mac and linux(here, os.name is 'posix') 
		#else: 
			## TODO UPDATE TO VM BOX 
		#	self.modelsim_path = "\\home\\ff\\intelFPGA_lite\\18.1\\modelsim_ase\\"

		