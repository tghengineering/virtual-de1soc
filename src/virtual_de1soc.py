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

	return configurationManager.get_config()

def run_simulation(screenIO, configuration):
	board = fpga.Board()

	sim = modelsim.BoardSimulator(board, configuration)
	#Seconds delay


	time_old = time.monotonic() 
	count = 0

	#while(count < 3):
	while(True):
		count += 1

		screenIO.renderBoard(board)
		time_new = time.monotonic()
		print("FPS : "+"{:2.2f}".format(1/(time_new-time_old)))
		time_old = time_new


		while(keystroke_detected()):
			value = get_key_stroke()
			if value in configuration["SW_key"]:
				sw_index = configuration["SW_key"].index(value)
				board.SW.value[sw_index] = not(board.SW.value[sw_index])
			if value in configuration["KEY_key"]:
				key_index = configuration["KEY_key"].index(value)
				board.KEY.value[key_index] = not(board.KEY.value[key_index])

		board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])

		sim.step()
		
		# time_new = time.monotonic()
		# delay = configuration["time_delay"] - (time_new - time_old)
		# if (delay > 0):
		# 	time.sleep(delay)
		# #print("Time ahead of the loop (seconds): "+str(delay))
		# if delay < 0:
		# 	print("System lagging by: "+str(-delay))
		# time_old = time_new




screenIO = ascii_ui.ScreenIO()
configuration = initialise(screenIO)

run_simulation(screenIO, configuration)

