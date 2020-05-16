import fpga
import modelsim
import config_manager
import ascii_ui
import os 
import time
import pathlib
import msvcrt

def keystroke_detected():
	return msvcrt.kbhit()

def get_key_stroke():
	return str(msvcrt.getwch())

def initialise(screenIO):
	configurationManager = config_manager.ConfigManager()
	configurationManager.load_config()
	screenIO.renderConfigMenu(configurationManager)
	configurationManager.get_modelsim_path()
	configurationManager.get_target_path()
	return configurationManager.config
	
def run_lib(screenIO, configuration):
	vlib = modelsim.VlibDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.clear()
	screenIO.renderMessage("Vlib finished")
	vmap = modelsim.VmapDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.renderMessage("Vmap finished")

def run_compile(screenIO, configuration):
	vlog = modelsim.VlogDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.renderMessage("Vlog finished")


def run_simulation(screenIO, configuration):
	board = fpga.Board()
	screenIO.clear()
	screenIO.renderMessage("Vsim starting...")

	sim = modelsim.VsimController(board, configuration)
	screenIO.clear()
	screenIO.renderMessage("Vsim running")
	

	#Seconds delay

	time_old = time.monotonic() 
	count = 0
	fps = 0 
	run = True
	while(run):
		count += 1

		screenIO.renderBoard(board,fps)
		time_new = time.monotonic()
		time_dealy = time_new-time_old
		fps = 1/(time_dealy)

		time_old = time_new


		while(keystroke_detected()):
			value = get_key_stroke()
			if value in configuration["SW_key"]:
				sw_index = configuration["SW_key"].index(value)
				board.SW.value[sw_index] = not(board.SW.value[sw_index])
			if value in configuration["KEY_key"]:
				key_index = configuration["KEY_key"].index(value)
				board.KEY.value[key_index] = not(board.KEY.value[key_index])
			if value in configuration["quit_key"]:
				run = False
		board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])


		#sim.step()
		sim.run(configuration["vsim_duration"])

		# time_new = time.monotonic()
		# delay = configuration["time_delay"] - (time_new - time_old)
		# if (delay > 0):
		# 	time.sleep(delay)
		# #print("Time ahead of the loop (seconds): "+str(delay))
		# if delay < 0:
		# 	print("System lagging by: "+str(-delay))
		# time_old = time_new
	sim.quitsim()





screenIO = ascii_ui.ScreenIO()

screenIO.renderMessage("Config loading...")

configuration = initialise(screenIO)

run_lib(screenIO, configuration)

run_compile(screenIO, configuration)

run_simulation(screenIO, configuration)

