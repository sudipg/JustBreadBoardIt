"""
Representation of a breadboard
"""

class Breadboard(object):
	"""docstring for Breadboard"""
	def __init__(self):
		super(Breadboard, self).__init__()
		self.number_of_rows = 50
		self.holes = {}
		self.right_red = {}
		self.right_blue = {}
		self.left_red = {}
		self.left_blue = {}
		self.components = {}

		# the standard center pins
		for x in range(1,11):
			for y in range(1, self.number_of_rows+1):
				self.holes[str(x).append('_'.append(str(y)))] = Hole(x, y)


		# the power lines
		for y in range(1, number_of_rows+1):
			right_blue[y] = Hole(0, y)
			right_red[y] = Hole(0, y)
			left_blue[y] = Hole(0, y)
			left_red[y] = Hole(0, y)

	def insert_pin(x, y, component, pin_number):
		self.holes[str(x).append('_'.append(str(y)))].insert_pin(pin_number, component)
		if not component in self.components.values():
			self.components[len(self.components)+1] = component

class Hole(object):
	"""docstring for Hole"""
	def __init__(self, x, y):
		super(Hole, self).__init__()
		self.x, self.y = x, y

	def insert_pin(self, pin_number, component):
		"""inserts a given component at the given pin number into THIS Hole"""
		self.pin_number = pin_number
		self.component = component

	def  get_item(self):
		"""returns the pin number and the component inserted at THIS Hole as a tuple"""
		try:
			return (self.pin_number, self.component)
		except Exception:
			return None
