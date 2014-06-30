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


positive_battery.insert_connection(negative_battery, 1)


"""
my_circuit.insert_connection(positive_battery, 1, led, 1)
my_circuit.insert_connection(led, 1, negative_battery, 1)
"""









"""
bat = my_circuit.insert_connection("battery", 2, 3, 1)

led = my_circuit.insert_connection("LED", 2, 1, 1)

res = my_circuit.insert_compon("resistor", 2, 2, 1)

my_circuit.insert_connection(bat, 1, res, 1)

my_circuit.insert_connection(res, 2, led, 1)

my_circuit.insert_connection(led, 2, bat, 2)
"""
