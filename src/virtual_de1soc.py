import fpga
import modelsim
import config
import ascii_ui
import os 
import time 
import keyboard
import pathlib

def initialise():
	configuration = config.configuration

	for index, key in enumerate(configuration):
		print("{0}) {1}: {2}".format(index+1, key, configuration[key]))

	userInput = input("Would you like to change any of these configuration? - Type in name of configuration or press ENTER to skip: ")

	while(userInput != ""):
		if userInput in configuration :
			newConfigValue = input("Changing {0} to: ".format(userInput))
			if newConfigValue != "":
				configuration[userInput] = newConfigValue
			else:
				print("Cannot change confinguration to blank")
		else:
			print("Invalid configuration key")
		userInput = input("Would you like to change any other configuration? - Number to select or press ENTER to skip: ")

	print("New configurations are")

	for index, key in enumerate(configuration):
		print("{0}) {1}: {2}".format(index+1, key, configuration[key]))

	return configuration


def run_simulation(configuration):
	board = fpga.Board()

	screen = ascii_ui.BoardWriter()

	sim = modelsim.BoardSimulator(board, configuration)
	#Seconds delay


	time_old = time.monotonic() 
	count = 0

	#while(count < 3):
	while(count < 3):
		count += 1

		screen.render(board)

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

configuration = initialise()

run_simulation(configuration)

