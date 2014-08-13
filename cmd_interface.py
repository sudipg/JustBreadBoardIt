#!/usr/bin/env python3

import circuit
import os
import visual_rep

da_circuit = circuit.Circuit()
name_dict = {}
print ('Welcome to JustBreadBoardit!')

"""NOTE: This is the core of the REPL, and the function that is is repeatedly called recursively. Has a few cool abilities like help, but really is
	an endless loop to call other things (as all REPLs are."""

def REPL():
	print ('')
	print ('You are at the main menu! Please type a command, or "help".')
	user_input = input('--> ')

	if user_input == "help":
		print ('')
		print ('You can type: "add" in order to add a component, "connect" in order to connect components you have added already, "remove_connection" to remove a connection you created, "print_components" to see the components that are in the circuit, or "print_connections" to see where your connections are!')
		print ('')
		print ('You can also type "clear" to clear the gunk off the terminal screen or "quit" to exit this program.')
		print ('')
		print ('Also, please note that before you connect components, they must have been added to the circuit with the "add" command.')
	elif user_input == "print_connections":
		print('')
		da_circuit.print_connections()
	elif user_input == "print_components":
		print ('')
		print ("List of components:")
		for part in name_dict:
			print (part + " is a " + name_dict[part][0])
	elif user_input == "remove_connection":
		remove()
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

"""NOTE: Subroutine called when the users asks REPL to add a part to the circuit. Remember, parts are added and THEN are connected!"""

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
			name_dict[add_name] = [to_add, component_reference]
			print('')
			print("Successfully added the " + to_add + " named " + add_name + " to the circuit! Returning to main menu.")
			REPL()

def connect():
	dabits = connect_helper('What is the first component that you would like to form a connection with?', 'What is the second component that you would like to form a connection with?', 'will be used in the connection?')
	print('')
	da_circuit.insert_connection(name_dict[dabits[0]][1], dabits[1], name_dict[dabits[2]][1], dabits[3])	
	REPL()

def remove():
	dabits = connect_helper('What is the first component in the connection you would like to remove?', 'What is the second component in the connection you would like to remove?', 'is part of the connection to be removed?')
	print('')
	da_circuit.remove_connection(name_dict[dabits[0]][1], dabits[1], name_dict[dabits[2]][1], dabits[3])
	REPL()

"""NOTE: the heart of how we insert and remove connections. This helper spits out values that the remove and add functions (in this file) 
	can use to call the removal and addition functions of the circuit object/ADT defined in circuit.py. This takes a few prompts to
	ask the user as well in order to be adaptable from an interface perspective. Also, note that this helper function calls another helper 
	function (scroll down). Horray for DRY and data abstraction."""

def connect_helper(prompt1, prompt2, prompt3):
	print ('')
	print (prompt1 + ' You can also type back to return to the main menu.')
	component_1_name = input("--> ")
	while component_1_name not in name_dict and component_1_name != "back":
		print ('')
		print ('There is no component with this name in the circuit. Try again.')
		component_1_name = input("--> ")
	if component_1_name == "back":
		REPL()
	
	component_1_pin_number = pin_number_getter(component_1_name, prompt3)

	print ('')
	print (prompt2 + ' You can also type back to return to the main menu.')
	component_2_name = input("--> ")
	while component_2_name not in name_dict and component_2_name != "back":
		print ('')
		print ('There is no component with this name in the circuit. Try again.')
		component_2_name = input("--> ")
	if component_2_name == "back":
		REPL()

	component_2_pin_number = pin_number_getter(component_2_name, prompt3)

	return [component_1_name, component_1_pin_number, component_2_name, component_2_pin_number]

"""NOTE: This is a helper function that is able to ask the user for the pin number they are interested in 
	for a certain component in the circuit. before we were having issues with strings getting through as 
	"pin numbers" and crashing the program when they were forced as numbers. This solves this and abstracts 
	the entire pin number retrieval process into a neat function."""

def pin_number_getter(component_name, purpose_string):
	while True:
		try:
			print ('')
			print ('Which pin number on ' + component_name + ' ' + purpose_string)
			component_pin_number = int(input('--> '))

		except ValueError:
			print ('')
			print ('Hey doofus! The pin number has to be a NUMBER!')
			continue

		break

	return component_pin_number

REPL()


