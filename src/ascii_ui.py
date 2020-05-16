# coding: utf-8
import os
	#return text_de1


class ScreenIO():
	def __init__(self):
		self.screen_clear = 'cls' if (os.name == 'nt') else 'clear' 


	
	def renderTop(self):
		print("┌────────────────────────────────────────────────────────────────────────────────────────────────────┐\n",end="")

	def renderLine(self,message):
		pad1 = round( ( 100 - len(message) ) / 2 )
		pad2 = 100 - pad1 - len(message)
		print("│"+" "*pad1+message+" "*pad2+"│\n",end="")

	def renderBottom(self):
		print("└────────────────────────────────────────────────────────────────────────────────────────────────────┘\n",end="")

	def renderEmpty(self):
		print("│                                                                                                    │\n",end="")

	def renderMessage(self,message):
		self.renderTop()
		self.renderEmpty()
		self.renderLine(message)
		self.renderEmpty()
		self.renderBottom()


	def renderConfigMenu(self, config, previousMessage = ""):
		os.system(self.screen_clear) 
		
		self.renderMessage("Welcome to the Virtual DE1SOC configuration menu view")


		menuString = " a) Continue with current setting (or enter)\n b) Reset settings from File\n c) Save to Config File\n d) Save to Config file and Continue\n e) Reset from Config File and Continue\n"
		print(menuString + str(config))
		print("Please select your option for the list above and then press enter...")
		print(previousMessage+"\n")
		userInput = input("").lower()

		if userInput == "a" or userInput == "b" or userInput == "c" or userInput == "d" or userInput == "e" or userInput == "":
			pass 
		elif userInput.isdigit():
			userInput = int(userInput)
		else:
			self.renderConfigMenu(config, "Invalid input given: {0}.".format(userInput))
		if userInput == "b":
			config.load_config()
			self.renderConfigMenu(config, "Configuration reloaded from file.")
		elif userInput == "c":
			config.save_config()
			self.renderConfigMenu(config, "Configuration saved to file.")
		elif userInput == "a" or userInput == "":
			os.system(self.screen_clear) 
		elif userInput == "d":
			config.save_config()
			os.system(self.screen_clear) 
		elif userInput == "e":
			config.load_config()
			os.system(self.screen_clear)
		elif userInput >= 0 and userInput <= 8:
			newConfigValue = input("New Configuration Value for {0}: ".format(config.get_config_value(userInput)))
			config.modify_config_value(userInput, newConfigValue)
			self.renderConfigMenu(config, "Configuration changed.")
		else:
			self.renderConfigMenu(config, "Invalid input given: {0}.".format(userInput))
		
	def clear(self):
		os.system(self.screen_clear) 

	def renderBoard(self,board,fps=0.0):
		shade1 = "░" 
		shade2 = "░░" 
		shade4 = "░░░░"
		light1 = "█"
		light2 = "██"
		light4 = "████"
		blank2 = "  "
		H0  = [(shade1 if (i) else light1 ) for i in (board.HEX0.value)]
		H1  = [(shade1 if (i) else light1 ) for i in (board.HEX1.value)]
		H2  = [(shade1 if (i) else light1 ) for i in (board.HEX2.value)]
		H3  = [(shade1 if (i) else light1 ) for i in (board.HEX3.value)]
		H4  = [(shade1 if (i) else light1 ) for i in (board.HEX4.value)]
		H5  = [(shade1 if (i) else light1 ) for i in (board.HEX5.value)]
		KEY = [(light4 if (i) else shade4 ) for i in (board.KEY.value) ]
		S   = [(light2 if (i) else blank2 ) for i in (board.SW.value)  ]
		s   = [(blank2 if (i) else light2 ) for i in (board.SW.value)  ]
		L   = [(light2 if (i) else shade2 ) for i in (board.LEDR.value)]
		CLK = [(light1 if ((board.CLOCK_50.value[0])) else shade1 )    ]
		text_de1 = [
		"┌────────────────────────────────────────────────────────────────────────────────────────────────────┐",
		"│   HEX5     HEX4        HEX3     HEX2        HEX1    HEX0                                 FPS:"+"{:>6.2f}".format(fps)+"│",
		"│┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐                                   ┌──┐│",
		"││  aaaa  │  bbbb  │  │  cccc  │  dddd  │  │  eeee  │  ffff  │                              CLK: │mm││",
		"││ a    b │ c    d │  │ e    f │ g    h │  │ i    j │ k    l │                                   └──┘│",
		"││ a    b │ c    d │  │ e    f │ g    h │  │ i    j │ k    l │                                       │",
		"││  aaaa  │  bbbb  │  │  cccc  │  dddd  │  │  eeee  │  ffff  │                                       │",
		"││ a    b │ c    d │  │ e    f │ g    h │  │ i    j │ k    l │                                       │",
		"││ a    b │ c    d │  │ e    f │ g    h │  │ i    j │ k    l │                                       │",
		"││  aaaa  │  bbbb  │  │  cccc  │  dddd  │  │  eeee  │  ffff  │                                       │",
		"│└─────────────────┘  └─────────────────┘  └─────────────────┘                                       │",
		"│ LEDR9  LEDR8  LEDR7  LEDR6  LEDR5  LEDR4  LEDR3  LEDR2  LEDR1  LEDR0                               │",
		"│┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐                             │",
		"││ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │                             │",
		"││ │L9│ │ │L8│ │ │L7│ │ │L6│ │ │L5│ │ │L4│ │ │L3│ │ │L2│ │ │L1│ │ │L0│ │                             │",
		"││ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │                             │",
		"│├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤┌──────┬──────┬──────┬──────┐│",
		"││ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ │ ┌──┐ ││┌────┐│┌────┐│┌────┐│┌────┐││",
		"││ │S9│ │ │S8│ │ │S7│ │ │S6│ │ │S5│ │ │S4│ │ │S3│ │ │S2│ │ │S1│ │ │S0│ │││KEY3│││KEY2│││KEY1│││KEY0│││",
		"││ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │ │  │ │││KEY3│││KEY2│││KEY1│││KEY0│││",
		"││ │s9│ │ │s8│ │ │s7│ │ │s6│ │ │s5│ │ │s4│ │ │s3│ │ │s2│ │ │s1│ │ │s0│ │││KEY3│││KEY2│││KEY1│││KEY0│││",
		"││ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ │ └──┘ ││└────┘│└────┘│└────┘│└────┘││",
		"│└──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘└──────┴──────┴──────┴──────┘│",
		"│  SW9    SW8    SW7    SW6    SW5    SW4    SW3    SW2    SW1    SW0     KEY3   KEY2   KEY1   KEY0  │",
		"└────────────────────────────────────────────────────────────────────────────────────────────────────┘"
		]
		text_de1[3]  = text_de1[3].replace("a",H5[0]).replace("b",H4[0]).replace("c",H3[0]).replace("d",H2[0]).replace("e",H1[0]).replace("f",H0[0]).replace("m",CLK[0])
		text_de1[4]  = text_de1[4].replace("a",H5[5]).replace("b",H5[1]).replace("c",H4[5]).replace("d",H4[1]).replace("e",H3[5]).replace("f",H3[1]).replace("g",H2[5]).replace("h",H2[1]).replace("i",H1[5]).replace("j",H1[1]).replace("k",H0[5]).replace("l",H0[1])
		text_de1[5]  = text_de1[5].replace("a",H5[5]).replace("b",H5[1]).replace("c",H4[5]).replace("d",H4[1]).replace("e",H3[5]).replace("f",H3[1]).replace("g",H2[5]).replace("h",H2[1]).replace("i",H1[5]).replace("j",H1[1]).replace("k",H0[5]).replace("l",H0[1])
		text_de1[6]  = text_de1[6].replace("a",H5[6]).replace("b",H4[6]).replace("c",H3[6]).replace("d",H2[6]).replace("e",H1[6]).replace("f",H0[6])
		text_de1[7]  = text_de1[7].replace("a",H5[4]).replace("b",H5[2]).replace("c",H4[4]).replace("d",H4[2]).replace("e",H3[4]).replace("f",H3[2]).replace("g",H2[4]).replace("h",H2[2]).replace("i",H1[4]).replace("j",H1[2]).replace("k",H0[4]).replace("l",H0[2])
		text_de1[8]  = text_de1[8].replace("a",H5[4]).replace("b",H5[2]).replace("c",H4[4]).replace("d",H4[2]).replace("e",H3[4]).replace("f",H3[2]).replace("g",H2[4]).replace("h",H2[2]).replace("i",H1[4]).replace("j",H1[2]).replace("k",H0[4]).replace("l",H0[2])
		text_de1[9]  = text_de1[9].replace("a",H5[3]).replace("b",H4[3]).replace("c",H3[3]).replace("d",H2[3]).replace("e",H1[3]).replace("f",H0[3])
		text_de1[14] = text_de1[14].replace("L9",L[9]).replace("L8",L[8]).replace("L7",L[7]).replace("L6",L[6]).replace("L5",L[5]).replace("L4",L[4]).replace("L3",L[3]).replace("L2",L[2]).replace("L1",L[1]).replace("L0",L[0])
		text_de1[18] = text_de1[18].replace("S9",S[9]).replace("S8",S[8]).replace("S7",S[7]).replace("S6",S[6]).replace("S5",S[5]).replace("S4",S[4]).replace("S3",S[3]).replace("S2",S[2]).replace("S1",S[1]).replace("S0",S[0]).replace("KEY3",KEY[3]).replace("KEY2",KEY[2]).replace("KEY1",KEY[1]).replace("KEY0",KEY[0])
		text_de1[19] = text_de1[19].replace("KEY3",KEY[3]).replace("KEY2",KEY[2]).replace("KEY1",KEY[1]).replace("KEY0",KEY[0])
		text_de1[20] = text_de1[20].replace("s9",s[9]).replace("s8",s[8]).replace("s7",s[7]).replace("s6",s[6]).replace("s5",s[5]).replace("s4",s[4]).replace("s3",s[3]).replace("s2",s[2]).replace("s1",s[1]).replace("s0",s[0]).replace("KEY3",KEY[3]).replace("KEY2",KEY[2]).replace("KEY1",KEY[1]).replace("KEY0",KEY[0])
		
		self.clear() 
		
		self.renderMessage("Virtual DE1SOC ascii view")

		for i in text_de1:
			print(i+"\n",end="")


