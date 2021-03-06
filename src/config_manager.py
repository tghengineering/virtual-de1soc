import os
import pathlib
import json

class ConfigManager():
	def load_config(self):
		with open('./config.json', 'r') as f:
			self.config = json.load(f)
			if "target_path" not in self.config: self.config["target_path"] = str(pathlib.Path.cwd())
			if "modelsim_path" not in self.config: self.config["modelsim_path"] = "C:\\intelFPGA_lite\\18.1\\modelsim_ase\\win32aloem\\" if os.name == "nt" else "/home/ff/intelFPGA_lite/18.1//modelsim_ase/linuxaloem/"
			self.configIndex = [k  for  k in  self.config.keys()]


	def save_config(self):
		with open('./config.json', 'w') as f:
			json.dump(self.config, f)


	def get_config_value(self, index):
		return self.configIndex[index]


	def modify_config_value(self, index, value):
		self.config[self.configIndex[index]] = value


	def set_types(self):
		self.config["modelsim_path"] = pathlib.Path(self.config["modelsim_path"])
		self.config["target_path"] = pathlib.Path(self.config["target_path"])
		self.config["frame_time"] = float(self.config["frame_time"])
		self.config["step_state"] = True if self.config["step_state"]=="True" else False


	def __str__(self):
		strConfig = "\n"
		for i, k in enumerate(self.config):
			strConfig += "{0:2.0f}) {1:_<24}: {2}\n".format(i, k, self.config[k])
		return strConfig