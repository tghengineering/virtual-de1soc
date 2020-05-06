class Port():
	def __init__(self, value, size, direction, name):
		# value = [b0 b1 b2 b3 ...]
		self.value = [value]*size
		self.direction = direction
		self.size = size
		self.name = name

	def get_value_lsb(self):
		return ''.join(map(lambda x: str(int(x)), self.value))

	def set_value_lsb(self,data):
		self.value = [True if  i=="1" else False for i in data]


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

	def get(self, port_name):
		return self.__dict__[port_name]

	def get_all(self):
		return self.__dict__.items()