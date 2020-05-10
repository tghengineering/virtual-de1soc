import fpga
import modelsim
import config_manager
import ascii_ui
import os 
import time 
import keyboard
import pathlib

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
	while(count < 3):
		count += 1

		screenIO.renderBoard(board)

		for x in range(len(configuration["SW_key"])):
			if keyboard.is_pressed(str(configuration["SW_key"][x])):
				board.SW.value[x] = not(board.SW.value[x])

		for x in range(len(configuration["KEY_key"])):
			if keyboard.is_pressed(str(configuration["KEY_key"][x])):
				board.KEY.value[x] = not(board.KEY.value[x])
		board.SW.value[0]=not(board.SW.value[0])
		board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])

		sim.run("50ms")
		
		time_new = time.monotonic()
		delay = configuration["time_delay"] - (time_new - time_old)
		if (delay > 0):
			time.sleep(delay)
		#print("Time ahead of the loop (seconds): "+str(delay))
		if delay < 0:
			print("System lagging by: "+str(-delay))
		time_old = time_new

screenIO = ascii_ui.ScreenIO()

configuration = initialise(screenIO)

run_simulation(screenIO, configuration)

