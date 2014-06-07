class Circuit(object):
	"""A Circuit representation"""

	def __init__(self):
		super(Circuit, self).__init__()
		self.components = []
		self.connetions = []

	def insert_connection(self, component1, component1_pin_number, component2, component2_pin_number):
		"""Only method to be used to insert a connection into the Circuit"""	
		new_connection = Connection(component1, component2)
		self.connections.append(new_connection)

	def insert_components(self, component_name, number_of_pins, x_length, y_length):
		"""Only method to be used to insert a component into the Circuit"""
		self.components.append(component)


class Component(object):
	"""docstring for Component"""
	def __init__(self, x_length, y_length, number_of_pins):
		super(Component, self).__init__()
		self.x_length, self.y_length = x_length, y_length
		self.number_of_pins = number_of_pins

	def insert_connection(target, target_pin_number):
		pass

	#need to use dicts


class Connection(object):
	"""docstring for Connection"""
	def __init__(self, component1, component2):
		super(Connection, self).__init__()
		self.component1 = component1
		self.component2 = component2

	@property
	def end1(self):
		return self.component1

	@property
	def end2(self):
		return self.component2