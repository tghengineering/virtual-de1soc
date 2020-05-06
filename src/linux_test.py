import fpga
import modelsim
import config
import ascii_ui
import os 
import time 
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

	board.SW.value[0]=not(board.SW.value[0])
	board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])

	sim.run("50ms")

	time_new = time.monotonic()
	delay = time_delay - (time_new - time_old)
	if (delay > 0):
		time.sleep(delay)
	print("Time ahead of the loop (seconds): "+str(delay))
	time_old = time_new