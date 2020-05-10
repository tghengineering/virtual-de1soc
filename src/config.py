import os
import pathlib

configuration = { }

configuration["vsim_step"] = True
configuration["visim_duration"] = "10ns"
configuration["lib_target_path"] = pathlib.Path.cwd()
configuration["lib_name"] = "work"
configuration["lib_top_level_entity"] = "MyProject"
configuration["modelsim_path"] = pathlib.Path("C://intelFPGA_lite//18.1//modelsim_ase//win32aloem//") if os.name == "nt" else pathlib.Path("/home/ff/intelFPGA_lite/18.1/modelsim_ase/linuxaloem/")
configuration["time_delay"] = 0.2
configuration["SW_key"] = ["0","9","8","7","6","5","4","3","2","1"]
configuration["KEY_key"] = ["p","o","i","u"]
