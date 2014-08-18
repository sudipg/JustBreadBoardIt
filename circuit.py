"""
This file contains most of the structures used to construct a circuit schematic
"""

# Sid: I did some quick changes and wrote a few comments. Sorry if it is a little hurried, but I had to go :/
# And the dogs are going to kill me in my sleep.
# HAI GUISE -Sherdil

class Circuit(object):
	"""A Circuit repr4esentation"""

	def __init__(self):
		super(Circuit, self).__init__()
		self.components = []
		self.connections = []

	#Hey, this is not well encapsulated. What if the stupid user makes a connection from A to B and then
	#from B to A (or from A to B twice)? -Sherdil 

	#Hey, new note. I made this function return different numbers in the case of a failure.
	#This is so that other programs can actually see WHY something failed. 
	#Sherdil, 7/7/2014
	def insert_connection(self, component1, component1_pin_number, component2, component2_pin_number):
		"""Only method to be used to insert a connection into the Circuit"""	
		
		#July 3, 2014, 11:42am (Yes, I'm coding at this hour. Bite me.)
		#New duplicate checker. Uses a new __eq__ in connections.
		for x in self.connections:
			if x == (Connection(component1, component1_pin_number, component2, component2_pin_number)):
				print ("This connection already exists!")
				return 1

		#Blocking connecting non existant pins/components.
		#Sherdil July 1, 2014, updated July 3
		if (component1 not in self.components) or (component2 not in self.components):
			print ("At least one of these components is not in the circuit!")
			return 2
		elif (component1_pin_number < 1 or component1_pin_number > component1.number_of_pins or component2_pin_number < 1 or component2_pin_number > component2.number_of_pins):
			print ("You are attempting to connect pins that do not exist!")
			return 3
		
		else:
			new_connection = Connection(component1, component1_pin_number, component2, component2_pin_number)
			self.connections.append(new_connection)
			component1.insert_connection(new_connection, component1_pin_number)
			component2.insert_connection(new_connection, component2_pin_number)
			print ("New connection made!")
			return new_connection
		#I modified the above line a bit because it did not call the func with the right amount of args.		

	def insert_component(self, component):
		"""Only method to be used to insert a component into the Circuit. Also returns the new component object"""
		for c in components:
			if c.component_name == component.component_name:
				return 'choose a different name...' #We cannot , for now, support multiple component names. maybe we can allow this once the highlighiting of components on canvas is implemented?
		self.components.append(component)
		return component

	
	#Hey, new note. I made this function return different numbers in the case of a failure.
	#This is so that other programs can actually see WHY something failed. 
	#Sherdil, 7/10/2014
	def remove_connection(self, component1, component1_pin_number, component2, component2_pin_number):
		"""Removes the given connection and its references from the relevant components"""
		test_connection = Connection(component1, component1_pin_number, component2, component2_pin_number)
		
		for x in self.connections:
			if x == test_connection:
				self.connections.remove(x)

				if len(component1.pins[component1_pin_number]) == 1:
					del component1.pins[component1_pin_number]
				else:
					for x in component1.pins[component1_pin_number]:
						if x == test_connection:
							component1.pins[component1_pin_number].remove(x)


				if len(component2.pins[component2_pin_number]) == 1:
					del component2.pins[component2_pin_number]
				else:
					for x in component2.pins[component2_pin_number]:
						if x == test_connection:
							component2.pins[component2_pin_number].remove(x)

				print ("Connection was removed!")
				return 1
			
		print ("You are attempting to remove a connection that does not exist!")
		return 2

	def print_connections(self):

		for x in self.connections:
			print ("There is a connection from " + str(x.component1.component_name) + " on pin " + str(x.component1_pin_number) + " to " + str(x.component2.component_name) + " on pin " + str(x.component2_pin_number) + " (and vice versa).")



#I feel like we should move component before Circuit. Components are the building blocks of circuits.
#IMHO, code should flow from least complicated to most compicated.
#Sherdil, July 1,2014
# go right ahead... I probably wrote this at 2AM
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
		self.id = Component.ID
		Component.ID += 1
		self.reach = max(x_length,y_length)
		self.component_name = component_name

	def insert_connection(self, target, source_pin_number):
		"""adds a connection from this component's """
		# I am guessing you know how you want to use this function. 

		if source_pin_number in self.pins.keys(): 
			self.pins[source_pin_number].append(target)
		else:
			self.pins[source_pin_number] = [target]
			# Nothing modified in the above line, but what is [target]?
			# making a list of connected this if it the the first one, appening otherwise


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

	#For the duplicate connection checker!
	def __eq__(self, other):
		if (self.component1 == other.component1 and self.component2 == other.component2) or (self.component1 == other.component2 and self.component2 == other.component1):
			if (self.component1_pin_number == other.component1_pin_number and self.component2_pin_number == other.component2_pin_number) or (self.component1_pin_number == other.component2_pin_number and self.component2_pin_number == other.component1_pin_number):
				return True
		return False


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

class Button(Component):
	"""docstring for Button"""
	def __init__(self, component_name):
		super(Button, self).__init__(component_name, 2, 2, 1)
		self.reach = 1

class Switchboard(Component):
	def __init__(self, component_name):
		super(Switchboard, self).__init__(component_name, 20, 5, 4)


"""		
my_circuit = Circuit()

#This is a list of components that we can use to test out our code.
positive_battery = Battery_positive("positive_battery")
negative_battery = Battery_negative("negative_battery")
led = LED("led")


my_circuit.insert_component(positive_battery)
my_circuit.insert_component(led)
my_circuit.insert_component(negative_battery)



my_circuit.insert_connection(positive_battery, 1, led, 1)
my_circuit.insert_connection(led, 1, negative_battery, 1)

#This should never happen! Sudip, we need to look at this. 
my_circuit.insert_connection(positive_battery, 13, negative_battery, 15)

#Right now this is not working. There should be an error that can't repeat a connection. It isn't triggering! 
my_circuit.remove_connection(positive_battery, 1, led, 1)
my_circuit.insert_connection(led, 1, positive_battery, 1)

#Hmm..this errors. For some reason.
#Sherdil, July 3
my_circuit.remove_connection(positive_battery, 1, led, 1)

print(len(my_circuit.connections))
"""
	
