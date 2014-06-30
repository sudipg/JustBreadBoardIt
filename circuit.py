"""
This file contains most of the structures used to construct a circuit schematic
"""

# Sid: I did some quick changes and wrote a few comments. Sorry if it is a little hurried, but I had to go :/
# And the dogs are going to kill me in my sleep.

class Circuit(object):
	"""A Circuit repr4esentation"""

	def __init__(self):
		super(Circuit, self).__init__()
		self.components = []
		self.connetions = []

	def insert_connection(self, component1, component1_pin_number, component2, component2_pin_number):
		"""Only method to be used to insert a connection into the Circuit"""	
		new_connection = Connection(component1, component1_pin_number, component2, component2_pin_number)
		self.connections.append(new_connection)
		component1.insert_connection(new_connection, component1_pin_number)
		component2.insert_connection(new_connection, component2_pin_number)
		#I modified the above line a bit because it did not call the func with the right amount of args.

		return new_connection

	def insert_component(self, component):
		"""Only method to be used to insert a component into the Circuit. Also returns the new component object"""
		self.components.append(component)

	def remove_connection(self, component1, component2):
		"""Removes the given connection and its references from the relevant components"""
		pass


class Component(object):
	"""docstring for Component"""
	ID = 1

	def __init__(self, component_name, number_of_pins, x_length, y_length):
		#We need a way of differentiating between two similar components. (What if we have 2 resistors.) An ID number will be fine.
		super(Component, self).__init__()
		# self.ID = rand_num or we could have a class field called id_gen that increments everytime a new object is created.
		self.x_length, self.y_length = x_length, y_length
		self.number_of_pins = number_of_pins
		self.pins = {}
		self.id = ID
		ID += 1
		self.reach = max(x_length,y_length)

	def insert_connection(self, target, source_pin_number):
		"""adds a connection from this component's """
		# I am guessing you know how you want to use this function. 
		if source_pin_number in self.pins.keys:
			self.pins[source_pin_number].append(target)
		else:
			self.pins[source_pin_number] = [target]
			# Nothing modified in the above line, but what is [target]?



class Connection(object):
	"""representationo of a standard electrical connection that joins two elements: mostly just a data holder. This is a component class, it's not to be used outside. Maybe we shoud make the class _Connection. Sorry for the long dostring; I don't remember how to do a multiline docstring."""
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


class Resistor(Component):
	"""docstring for Resistor"""
	def __init__(self, component_name):
		super(Resistor, self).__init__(component_name, 2, 2, 1)
		self.reach = 6 # reach defines the max distance that can be maintained between its two pins

class Capacitor(Component):
	"""docstring for Capacitor"""
	def __init__(self, component_name):
		super(Capacitor, self).__init__(component_name, 2,2,1)		
		self.reach = 3

class Battery_positive(Component):
	"""docstring for Battery_positive"""
	def __init__(self, component_name):
		super(Battery_positive, self).__init__(component_name, 1, 1, 1)
	
class Battery_negative(Component):
	"""docstring for Battery_negative"""
	def __init__(self, component_name):
		super(Battery_negative, self).__init__(component_name, 1, 1, 1)
		

class LED(Component):
	"""docstring for LED"""
	def __init__(self, component_name):
		super(LED, self).__init__(component_name, 2, 2, 1)
		self.reach = 4

class Button(object):
	"""docstring for Button"""
	def __init__(self, component_name):
		super(Button, self).__init__(component_name, 2, 2, 1)
		self.reach = 1

		
		
