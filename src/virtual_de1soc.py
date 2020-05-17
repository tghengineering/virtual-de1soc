import fpga
import modelsim
import config_manager
import ascii_ui
import os 
import time
import pathlib
# import msvcrt
import keyboard

# def keystroke_detected():
# 	return msvcrt.kbhit()

def get_key_stroke():
	# return str(msvcrt.getwch())
	#  keyboard.is_pressed
	keyevents = keyboard.stop_recording()
	keyboard.start_recording()
	keylist = []
	for event in keyevents:
		if event.event_type == "down":
			if event.name not in keylist:
				keylist.append(event.name.lower())
	return keylist


def initialise(screenIO):
	configurationManager = config_manager.ConfigManager()
	configurationManager.load_config()
	screenIO.renderConfigMenu(configurationManager)
	configurationManager.set_types()
	return configurationManager.config

def run_lib(screenIO, configuration):
	modelsim.VlibDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.clear()
	screenIO.renderMessage("Vlib finished")
	modelsim.VmapDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.renderMessage("Vmap finished")

def run_compile(screenIO, configuration):
	vlog = modelsim.VlogDriver(configuration["modelsim_path"], target_path = configuration["target_path"] )
	screenIO.renderMessage("Vlog finished")
	screenIO.renderMessage(vlog.outs)
	time.sleep(10)
# def key_update(board, configuration):


def run_simulation(screenIO, configuration):
	board = fpga.Board()
	screenIO.clear()
	screenIO.renderMessage("Vsim starting...")

	sim = modelsim.VsimController(board, configuration)
	screenIO.clear()
	screenIO.renderMessage("Vsim running")
	

	keyboard.start_recording()

	time_old = time.monotonic() 
	count = 0
	fps = 0 
	run = True
	while(run):
		count += 1
		pause_loop =  configuration["step_state"] 
	
		if( configuration["step_state"]   ):
			while pause_loop == True:
				keyevents = get_key_stroke()
				if len(keyevents) > 0:
					for value in keyevents:
						if value in configuration["SW_key"]:
							sw_index = configuration["SW_key"].index(value)
							board.SW.value[sw_index] = not(board.SW.value[sw_index])
						if value in configuration["KEY_key"]:
							key_index = configuration["KEY_key"].index(value)
							board.KEY.value[key_index] = not(board.KEY.value[key_index])
						if value in configuration["quit_key"]:
							run = False
						if value in configuration["forward_key"]:
							pause_loop = False
						if value in configuration["step_key"]:
							configuration["step_state"] = not(configuration["step_state"])
							pause_loop = False
						if value in configuration["CLK_key"]:
							board.CLOCK_50.value[0] = not(board.CLOCK_50.value[0])
				screenIO.renderBoard(board,fps)
				screenIO.renderMessage("STEP MODE!!!! Count: "+str(count))

				time_new = time.monotonic()
				time_dealy = time_new-time_old
				time_lead = configuration["frame_time"] - time_dealy
				if (time_lead > 0):
					# print(time_lead)
					time.sleep(time_lead)

				time_new = time.monotonic()
				time_dealy = time_new-time_old
				fps = 1/(time_dealy)

				time_old = time_new

		else:
			keyevents = get_key_stroke()
			if len(keyevents) > 0:
				for value in keyevents:
					if value in configuration["SW_key"]:
						sw_index = configuration["SW_key"].index(value)
						board.SW.value[sw_index] = not(board.SW.value[sw_index])
					if value in configuration["KEY_key"]:
						key_index = configuration["KEY_key"].index(value)
						board.KEY.value[key_index] = not(board.KEY.value[key_index])
					if value in configuration["quit_key"]:
						run = False
					if value in configuration["forward_key"]:
						pause_loop = False
					if value in configuration["step_key"]:
						configuration["step_state"] = not(configuration["step_state"])

			board.CLOCK_50.value[0]=not(board.CLOCK_50.value[0])



		#sim.step()
		sim.run(configuration["vsim_duration"])

		screenIO.renderBoard(board,fps)
		if configuration["step_state"]:
			screenIO.renderMessage("STEP UPDATED! Count: "+str(count))
		else:
			screenIO.renderMessage("Continuous mode")


		time_new = time.monotonic()
		time_dealy = time_new-time_old
		time_lead = configuration["frame_time"] - time_dealy
		if (time_lead > 0):
			# print(time_lead)
			time.sleep(time_lead)

		time_new = time.monotonic()
		time_dealy = time_new-time_old
		fps = 1/(time_dealy)

		time_old = time_new
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

