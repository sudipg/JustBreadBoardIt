import circuit


"""
This file is meant serve as a testing ground and as a future reference for the correct implementation of the circuits
defined in circuit.py 
--June 8
"""

my_circuit = circuit.Circuit()

#This is a list of components that we can use to test out our code.
positive_battery = circuit.Battery_positive("positive_battery")
negative_battery = circuit.Battery_negative("negative_battery")
led = circuit.LED("led")


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
print (my_circuit.connections[1] == circuit.Connection(positive_battery, 1, led, 1))

my_circuit.remove_connection(positive_battery, 1, led, 1)











"""
bat = my_circuit.insert_connection("battery", 2, 3, 1)

led = my_circuit.insert_connection("LED", 2, 1, 1)

res = my_circuit.insert_compon("resistor", 2, 2, 1)

my_circuit.insert_connection(bat, 1, res, 1)

my_circuit.insert_connection(res, 2, led, 1)

my_circuit.insert_connection(led, 2, bat, 2)

"""
