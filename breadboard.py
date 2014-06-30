"""
Representation of a breadboard
"""
import disjoint_set as ds

class Breadboard(object):
	"""docstring for Breadboard"""
	def __init__(self):
		super(Breadboard, self).__init__()
		self.number_of_rows = 50
		self.holes = {}
		self.components = {}

		# the standard center pins
		"""Holes saved in dictionary with keys saved as x_y as a string"""
		for x in range(1,15):
			for y in range(1, self.number_of_rows+1):
				self.holes[str(x).append('_'.append(str(y)))] = Hole(x, y)

		# setup disjoint sets
		sets = ds.DisjointSets(14*number_of_rows)


	def insert_pin(x, y, component, pin_number):
		self.holes[str(x).append('_'.append(str(y)))].insert_pin(pin_number, component)
		if not component in self.components.values():
			self.components[len(self.components)+1] = component

	def is_connected(x1, y1, x2, y2):
		"""For checking if two given points in the center of the breadboard are connected electrically"""
		pass

	def find_connected_in_range(hole, x1, y1, range):
		"""returns a list of tuples of coordinates of rearby conneced holes connected to the given hole, within range of x1, y1"""
		pass

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
