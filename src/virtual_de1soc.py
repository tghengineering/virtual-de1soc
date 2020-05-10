import fpga
import modelsim
import config
import ascii_ui
import os 
import time 
import keyboard
import pathlib

def run_simulation(config):
	board = fpga.Board()

	screen = ascii_ui.BoardWriter()

	sim = modelsim.BoardSimulator(board,config)
	#Seconds delay


	time_old = time.monotonic() 
	count = 0

	#while(count < 3):
	while(count < 3):
		count += 1

		screen.render(board)

		for x in range(len(config["SW_key"])):
			if keyboard.is_pressed(str(config["SW_key"][x])):
				board.SW.value[x] = not(board.SW.value[x])

		for x in range(len(config["KEY_key"])):
			if keyboard.is_pressed(str(config["KEY_key"][x])):
				board.KEY.value[x] = not(board.KEY.value[x])
		board.SW.value[0]=not(board.SW.value[0])
		board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])

		sim.run("50ms")
		
		time_new = time.monotonic()
		delay = config["time_delay"] - (time_new - time_old)
		if (delay > 0):
			time.sleep(delay)
		#print("Time ahead of the loop (seconds): "+str(delay))
		if delay < 0:
			print("System lagging by: "+str(-delay))
		time_old = time_new


config = config.configuration

run_simulation(config)

