import os


class Config():
	def __init__(self):
		#self.config_file_name = "virtual_de1soc.txt"
			# for windows 
		if os.name == 'nt': 
			self.modelsim_path = "C:\\intelFPGA_lite\\18.1\\modelsim_ase\\win32aloem\\" 
			# for mac and linux(here, os.name is 'posix') 
		else: 
			self.modelsim_path = "C:\\intelFPGA_lite\\18.1\\modelsim_ase\\win32aloem\\"
		
		
		self.top_level_entity= "MyProject"
		#self.modelsim_modules = ["MyProject"]
		
		#if (os.path.exists(self.config_file_name)):
		#	with open(self.config_file_name,"r") as file:
		#		print(file.read())
		#else:
		#	print("no config file exists")

	#def check_modelsim_path(self):
	#	check = os.path.exists(self.modelsim_path) \
	#		& os.path.exists(self.modelsim_path+"vlib.exe") \
	#		& os.path.exists(self.modelsim_path+"vmap.exe") \
	#		& os.path.exists(self.modelsim_path+"vlog.exe") \
	#		& os.path.exists(self.modelsim_path+"vsim.exe")
	#	return check


	#def list_modelsim_modules(self):
	#	self.modelsim_modules=[]
	#	if os.path.exists("work/_info"):
	#		with open("work/_info","  r") as info_file:
	#			for line in info_file.readlines():
	#				if (line[0] == "v"):
	#					#print(line[1:(len(line)-1)])
	#					self.modelsim_modules.append(line[1:(len(line)-1)])