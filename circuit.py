"""
This file contains most of the structures used to construct a circuit schematic
"""
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
		self.components.append(component_name, number_of_pins, x_length, y_length)


class Component(object):
	"""docstring for Component"""
	def __init__(self, component_name, number_of_pins, x_length, y_length):
		super(Component, self).__init__()
		self.x_length, self.y_length = x_length, y_length
		self.number_of_pins = number_of_pins
		self.pins = {}

	def insert_connection(target, target_pin_number, source_pin_number):
		


class Connection(object):
	"""representationo of a standard electrical connection that joins two elements"""
	def __init__(self, component1, component1_pin_number, component2, component2_pin_number):
		super(Connection, self).__init__()
		self.component1 = component1
		self.component2 = component2
		self.component1_pin_number = component1_pin_number
		self.component2_pin_number = component2_pin_number

	@property
	def end1(self):
		"""returns the first connected component as a Component object"""
		return self.component1

	@property
	def end2(self):
		"""returns the second connected component as a Component object"""
		return self.component2