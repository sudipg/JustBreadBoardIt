#!/usr/bin/env python3

import circuit
import os

da_circuit = circuit.Circuit()
name_dict = {}
print ('Welcome to JustBreadBoardit!')

def REPL():
	print ('')
	print ('You are at the main menu! Please type a command, or "help".')
	user_input = input('--> ')

	if user_input == "help":
		print ('')
		print ('You can type "add" in order to add a component, "connect" in order to connect components you have added already, or "print" to see where your connections are!')
	elif user_input == "print":
		print('')
		da_circuit.print_connections()
	elif user_input == "add":
		add()
	elif user_input == "connect":
		connect()
	elif user_input == "clear":
		os.system('cls' if os.name=='nt' else 'clear')
	elif user_input == "quit":
		exit(0)
	else:
		print('')
		print ("I'm sorry, that command is invalid!")
	
	REPL()

def add():
	print("")
	print ('What type of component would you like to add? Type "help" for a list of types, or "back" to go back.')
	
	component_dict = {'resistor' : circuit.Resistor, 'capacitor' : circuit.Capacitor, 'positive_battery' : circuit.Battery_positive, 'negative_battery' : circuit.Battery_negative, 'led' : circuit.LED, 'button' : circuit.Button}

	to_add = input('--> ')
	if to_add == 'help':
		print ('')
		print ("These are the types of components you can add:")
		print ("resistor")
		print ("capacitor")
		print ("positive_battery")
		print ("negative_battery")
		print ("led")
		print ("button")
		print ("Please input the name of one of these components at the prompt in order to add them")
		add()
	
	if to_add == "back":
		REPL()

	else:
		if to_add not in component_dict:
			print('')
			print ("Sorry, it looks like that isn't a valid component type!")
			add()
		else:
			print ('')
			print ('Please name the ' + to_add + ' you want to add.')
			add_name = input('--> ')
			while add_name in name_dict:
				print('')
				print('Sorry, another component with that same name is already in the circuit!')
				print('Please choose another name:')
				add_name = input('--> ')
			component_reference = component_dict[to_add](add_name)
			da_circuit.insert_component(component_reference)
			name_dict[add_name] = component_reference
			print('')
			print("Successfully added the " + to_add + " named " + add_name + " to the circuit! Returning to main menu.")
			REPL()

def connect():
	print ('')
	print ('What is the first component that you would like to form a connection with? You can also type back to return to the main menu.')
	component_1_name = input("--> ")
	while component_1_name not in name_dict and component_1_name != "cancel":
		print ('')
		print ('There is no component with this name in the circuit. Try again.')
		component_1_name = input("--> ")
	if component_1_name == "cancel":
		REPL()
	print ('')
	print ('Which pin number on ' + component_1_name + ' will be used in the connection?')
	component_1_pin_number = input('--> ')

	print ('')
	print ('What is the second component that you would like to form a connection with? You can also type back to return to the main menu.')
	component_2_name = input("--> ")
	while component_2_name not in name_dict and component_2_name != "cancel":
		print ('')
		print ('There is no component with this name in the circuit. Try again.')
		component_2_name = input("--> ")
	if component_2_name == "cancel":
		REPL()
	print ('')
	print ('Which pin number on ' + component_2_name + ' will be used in the connection?')
	component_2_pin_number = input('--> ')

	print('')
	da_circuit.insert_connection(name_dict[component_1_name], int(component_1_pin_number), name_dict[component_2_name], int(component_2_pin_number))
	REPL()





REPL()


