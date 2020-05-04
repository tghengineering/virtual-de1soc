class Port():
	def __init__(self, value, size, direction, name):
		self.value = [value]*size
		self.direction = direction
		self.size = size
		self.name = name

	def value_str(self):
		return ''.join(map(lambda x: str(int(x)), self.value))

	def value_set(self,data):
		self.value = [True if  i=="1" else False for i in data[::-1]]


class Board():
	def __init__(self):
		self.SW   = Port(False,10,"input","SW")
		self.LEDR = Port(False,10,"output","LEDR")
		self.KEY  = Port(True,4,"input","KEY")
		self.HEX0 = Port(True,7,"output","HEX0")
		self.HEX1 = Port(True,7,"output","HEX1")
		self.HEX2 = Port(True,7,"output","HEX2")
		self.HEX3 = Port(True,7,"output","HEX3")
		self.HEX4 = Port(True,7,"output","HEX4")
		self.HEX5 = Port(True,7,"output","HEX5")
		self.CLOCK_50 = Port(False,1,"input","CLOCK_50")
