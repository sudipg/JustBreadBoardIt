"""This is the file that runs the graphical user interface as opposed to the command line interface you get in cmd_interface.py. We used
Tkinter to build this, with a lot of inspiration from the command line interface. Also note that the terminal is used still in this version,
the user just doesn't interact with it. It's used to display lists to make the user's life much easier."""

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import circuit
import visual_rep


os.system('cls' if os.name=='nt' else 'clear')
print("Look here every now and then! We like to print lists to this terminal to help you see what's in your circuit.")

da_circuit = circuit.Circuit()

name_dict = {}

root = Tk()

da_rep = visual_rep.Visual_rep(root)

#Creating our root window.
root.title("JustBreadBoardIt!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

"""SECTION NOTE:These are the functions that get called when the user pushes one of the buttons on the root window. Each one aligns to one of the buttons.
Note that there are many helper functions bellow these core functions to better implement the principles of DRY and data abstraction. Without reading
those too, these won't make all that much sense."""

"""This function lets the user add a component to the circuit (again, just like with the command line, you must add components THEN connect them.)"""
def GUI_add(*args):
	print_components_helper()

	component_dict = {'resistor' : circuit.Resistor, 'capacitor' : circuit.Capacitor, 'positive_battery' : circuit.Battery_positive, 'negative_battery' : circuit.Battery_negative, 'led' : circuit.LED, 'button' : circuit.Button}

	add_window = Toplevel(root)
	add_frame = ttk.Frame(add_window, padding="3 3 12 12")
	add_frame.grid(column=0, row=0, sticky=(N, W, S, E))

	ttk.Label(add_frame, text="What kind of component would you like to add?").grid(column=1, row=1, sticky=W)
	
	component_type = ttk.Combobox(add_frame)
	component_type.grid(column=1, row=2, sticky=W)
	component_type['values'] =  ('resistor', 'capacitor', 'positive_battery', 'negative_battery', 'led', 'button')
	component_type.set('resistor')

	ttk.Label(add_frame, text="What will it be called?").grid(column=1, row=3, sticky=W)

	component_name = ttk.Entry(add_frame)
	component_name.grid(column=1, row = 4, sticky=W)

	#A function called when the user hits the final button.
	def add_button():
		if component_name.get() == '':
			warning("Whoah there tiger, looks like you forget a name there!")
		elif component_name.get() in name_dict:
			warning("Sorry, looks like there's a part with that name already in the circuit.")
		else:
			component_reference = component_dict[component_type.get()](component_name.get())
			da_circuit.insert_component(component_reference)
			name_dict[component_name.get()] = [component_type.get(), component_reference]
			
			da_rep.insert(component_name.get(), component_reference.x_length, component_reference.y_length)

			print_components_helper()
			FYI("Successfully added a " + component_type.get() + " named " + component_name.get() + "! Please check the terminal window for an updated list.")
			
	ttk.Button(add_frame, text="Add part!", command=add_button).grid(column=1, row=5, sticky=W)
	ttk.Button(add_frame, text="Back", command= lambda: add_window.destroy()).grid(column=2, row=5, sticky = W)


"""To insert a connection between two parts of the circuit. You REALLY need to read insert_helper to get this."""
def GUI_insert(*args):

	#The function that activates when the user presses the final button to create the connection in the new window.
	#Yes, it has to be in this format. 
	def insert_button(component_1_name, pin_1, component_2_name, pin_2):
		if component_1_name.get() == '' or component_2_name.get() == '':
			warning("Oops..looks like you forgot a component name there!")
		else:
			try:
				tester = da_circuit.insert_connection(name_dict[component_1_name.get()][1], int(pin_1.get()), name_dict[component_2_name.get()][1], int(pin_2.get()))
				print_connections_helper()
				if isinstance(tester, int):
					if tester == 1:
						warning("Sorry, that connection already exists!") 
					elif tester == 3:
						warning("Sorry, looks like you're trying to conenct pins that don't exist!") 
				else:
					
					da_rep.connect(component_1_name.get(), int(pin_1.get()), component_2_name.get(), int(pin_2.get()))

					FYI("New connections made! Check the terminal window for an updated list.")
			except ValueError:
				warning("Sorry, check that your pin numbers exist and are actually numbers!")

	insert_helper("involved in the new connection", "Make connection!", insert_button)

"""To remove a connection between two parts of the circuit. You REALLY need to read insert_helper to get this."""
def GUI_remove(*args):
	
	def remove_button(component_1_name, pin_1, component_2_name, pin_2):
		if component_1_name.get() == '' or component_2_name.get() == '':
			warning("Oops..looks like you forgot a component name there!")
		else:
			try:
				tester = da_circuit.remove_connection(name_dict[component_1_name.get()][1], int(pin_1.get()), name_dict[component_2_name.get()][1], int(pin_2.get()))
				print_connections_helper()
				if tester == 1:
					
					da_rep.remove(component_1_name.get(), int(pin_1.get()), component_2_name.get(), int(pin_2.get()))

					FYI("Connection successfully removed. Please check the terminal window for an updated list of connections.")
				elif tester == 2:
					warning("Whoops! You're trying to remove a connection that doesn't exist.")
					
			except ValueError:
				warning("Sorry, check that your pin numbers exist and are actually numbers!")

	insert_helper("involved in the removed connection", "Remove connection!", remove_button)

"""Just prints a list of connections to the terminal for the user to see."""
def GUI_connections(*args):
	print_connections_helper()
	FYI("A list of connections currently in the circuit has been printed to the terminal screen.")

"""Just prints a list of components to the terminal for the user to see."""
def GUI_components(*args):
	print_components_helper()
	FYI("A list of components currently in the circuit has been printed to the terminal screen.")

"""Lets the user quit the program."""
def GUI_quit(*args):
	root.destroy()
	exit(0)

"""SECTION NOTE: These are the all important helper functions."""

#Just pops up a warning box with the string inmessage.
def warning(inmessage):
	messagebox.showinfo(message=inmessage, icon='error', title="Uh-oh...")

#Just pops up a notification dialogue similar to warning function. 
def FYI(inmessage):
	messagebox.showinfo(message=inmessage, icon='info', title="FYI...")

#Abstracts the idea of printing a list of connection to the terminal. It's done quite a bit.
def print_connections_helper():
	os.system('cls' if os.name=='nt' else 'clear')
	print ("Current list of all connections in circuit:")
	print ("")
	da_circuit.print_connections()
	print ("")
	print ("End of list.")

#Abstracts the idea of printing a list of components to the terminal. It's done quite a bit.
def print_components_helper():
	os.system('cls' if os.name=='nt' else 'clear')
	print("Current list of all components in the circuit...")
	print ("")
	for part in name_dict:
			print (part + " is a " + name_dict[part][0])
	print ("")
	print ("End of list.")

"""The biggie. Grabbing a pair of pins and components is a very common task. This abstracts it away. The general
	set up of the window in these cases is always the same, so we just take in a partial prompt string that changes 
	depending on the box's purpose. We also take in a command function that executes on the final button press, but due to 
	the fact that Python is lexically scoped, we need that command function to take in four values (the pair of components and
	pins that this window grabs from the user.) Got all that? T.T"""

def insert_helper(task_string, button_text, command_function):
	print_connections_helper()

	insert_window = Toplevel(root)
	insert_frame = ttk.Frame(insert_window, padding="3 3 12 12")
	insert_frame.grid(column=0, row=0, sticky=(N, W, S, E))

	ttk.Label(insert_frame, text="What is the name of the first component in the circuit " + task_string+ "?").grid(column=1, row=1, sticky=W)

	component_1_name = ttk.Combobox(insert_frame)
	component_1_name['values'] = tuple(name_dict.keys())
	component_1_name.grid(column=1, row=2, sticky=W)

	ttk.Label(insert_frame, text="   On what pin number?").grid(column=2, row=1, sticky=W)

	pin_1 = ttk.Entry(insert_frame)
	pin_1.grid(column=2, row=2, sticky=W)

	ttk.Label(insert_frame, text="What is the name of the second component in the circuit " + task_string+ "?").grid(column=1, row=3, sticky=W)

	component_2_name = ttk.Combobox(insert_frame)
	component_2_name['values'] = tuple(name_dict.keys())
	component_2_name.grid(column=1, row=4, sticky=W)

	ttk.Label(insert_frame, text="   On what pin number?").grid(column=2, row=3, sticky=W)

	pin_2 = ttk.Entry(insert_frame)
	pin_2.grid(column=2, row=4, sticky=W)

	#Small thing where we pass value into the command function, becasue TK requires a function that takes no arguments.
	#PYTHON, WHY YOU NO LET ME PICK DYNAMIC SCOPING?!?!?!?! Rawr. Guess that would break a lot of other things though....
	holder_function = lambda: command_function(component_1_name, pin_1, component_2_name, pin_2)
	ttk.Button(insert_frame, text=button_text, command = holder_function).grid(column=1, row=5, sticky=W)
	
	ttk.Button(insert_frame, text="Back", command=lambda: insert_window.destroy()).grid(column=2, row=5, sticky=W)

"""Just setting up the root window."""

ttk.Label(mainframe, text="Welcome to JustBreadBoardIt! What will you do?").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Add component to circuit", command=GUI_add).grid(column=1, row = 2, sticky=W)
ttk.Button(mainframe, text="Connect two components in circuit", command=GUI_insert).grid(column=2, row = 2, sticky=W)
ttk.Button(mainframe, text="Remove a connection", command=GUI_remove).grid(column=3, row = 2, sticky=W)
ttk.Button(mainframe, text="Print components in circuit", command=GUI_components).grid(column=1, row = 3, sticky=W)
ttk.Button(mainframe, text="Print connections in circuit", command=GUI_connections).grid(column=2, row = 3, sticky=W)
ttk.Button(mainframe, text="Quit program", command=GUI_quit).grid(column=3, row = 3, sticky=W)


root.mainloop()