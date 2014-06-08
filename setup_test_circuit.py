import circuit


"""
This file is meant serve as a testing ground and as a future reference for the correct implementation of the circuits
defined in circuit.py 
--June 8
"""

my_circuit = circuit.Circuit()

bat = my_circuit.insert_component("battery", 2, 3, 1)

led = my_circuit.insert_component("LED", 2, 1, 1)

res = my_circuit.insert_component("resistor", 2, 2, 1)

my_circuit.insert_connection(bat, 1, res, 1)

my_circuit.insert_connection(res, 2, led, 1)

my_circuit.insert_connection(led, 2, bat, 2)
