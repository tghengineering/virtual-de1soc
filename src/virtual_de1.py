import modelsim
import fpga
import config
import ascii_ui
import os 
import time 
import keyboard


board = fpga.Board()
config = config.Config()

modelsim.VlibDriver(config)
modelsim.VmapDriver(config)
modelsim.VlogDriver(config)

sim = modelsim.VsimDriver(board,config)

tdealy = 0.01
#SW_key = ["0","9","8","7","6","5","4","3","2","1"]
SW_key = ["0","9","8","7","6","5","4","3","2","1"]
KEY_key = ["p","o","i","u"]

while(True):
	sim.group_force()
	sim.run("100ns")
	sim.group_examine()
	 
	ascii_ui.text_de1(board)

	time.sleep(0.01)

	for x in range(len(SW_key)):
		if keyboard.is_pressed(str(SW_key[x])):
			board.SW.value[x] = not(board.SW.value[x])

	for x in range(len(KEY_key)):
		if keyboard.is_pressed(str(KEY_key[x])):
			board.KEY.value[x] = not(board.KEY.value[x])

	board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])