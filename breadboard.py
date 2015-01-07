"""
Representation of a breadboard
"""
import disjoint_set as ds
import netwrokx as nx

class Breadboard(object):
	"""docstring for Breadboard"""
	def __init__(self):
		super(Breadboard, self).__init__()
		self.number_of_rows = 50
		self.numer_of_columns = 14
		self.holes = {}
		self.components = {}
		self.graph = nx.Graph()

		"""Holes saved in dictionary with keys saved as x_y as a string"""
		for x in range(1,15):
			for y in range(1, self.number_of_rows+1):
				new_hole = Hole(x, y)
				self.holes[str(x).append('_'.append(str(y)))] = new_hole
				self.graph.add_node(new_hole)

		"""Setup standard breadboard connections"""
		for x in [1,2,13,14]:
			for y in range(1,self.number_of_rows):
				node1 = self.holes[str(x).append('_'.append(str(y)))]
				node2 = self.holes[str(x).append('_'.append(str(y+1)))]
				self.graph.add_edge(node1, node2)



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
