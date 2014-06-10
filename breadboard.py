"""
Representation of a breadboard
"""

class Breadboard(object):
	"""docstring for Breadboard"""
	def __init__(self):
		super(Breadboard, self).__init__()
		self.number_of_rows = 20
		

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
