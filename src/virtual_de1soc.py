import fpga
import modelsim
import config
import ascii_ui
import os 
import time 
import keyboard
import pathlib


board = fpga.Board()
config = config.Config()
sim = modelsim.BoardSimulator(board,config)
#Seconds delay
time_delay = 0.2
#SW_key = ["0","9","8","7","6","5","4","3","2","1"]
SW_key = ["0","9","8","7","6","5","4","3","2","1"]
KEY_key = ["p","o","i","u"]

time_old = time.monotonic() 
count = 0

while(count < 10):
	count += 1

	ascii_ui.render(board)

	for x in range(len(SW_key)):
		if keyboard.is_pressed(str(SW_key[x])):
			board.SW.value[x] = not(board.SW.value[x])

	for x in range(len(KEY_key)):
		if keyboard.is_pressed(str(KEY_key[x])):
			board.KEY.value[x] = not(board.KEY.value[x])
	board.SW.value[0]=not(board.SW.value[0])
	board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])

	sim.run("50ms")
	
	time_new = time.monotonic()
	delay = time_delay - (time_new - time_old)
	if (delay > 0):
		time.sleep(delay)
	print("Time ahead of the loop (seconds): "+str(delay))
	time_old = time_new