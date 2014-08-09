import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import circuit

os.system('cls' if os.name=='nt' else 'clear')
print("Look here every now and then! We like to print lists to this terminal to help you see what's in your circuit.")

da_circuit = circuit.Circuit()
name_dict = {}

root = Tk()

root.title("JustBreadBoardIt!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))


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

	def add_button():
		if component_name.get() == '':
			warning("Whoah there tiger, looks like you forget a name there!")
		elif component_name.get() in name_dict:
			warning("Sorry, looks like there's a part with that name already in the circuit.")
		else:
			component_reference = component_dict[component_type.get()](component_name.get())
			da_circuit.insert_component(component_reference)
			name_dict[component_name.get()] = [component_type.get(), component_reference]
			print_components_helper()
			FYI("Successfully added a " + component_type.get() + " named " + component_name.get() + "! Please check the terminal window for an updated list.")
			
	ttk.Button(add_frame, text="Add part!", command=add_button).grid(column=1, row=5, sticky=W)
	ttk.Button(add_frame, text="Back", command= lambda: add_window.destroy()).grid(column=2, row=5, sticky = W)


def GUI_insert(*args):

	print_connections_helper()

	insert_window = Toplevel(root)
	insert_frame = ttk.Frame(insert_window, padding="3 3 12 12")
	insert_frame.grid(column=0, row=0, sticky=(N, W, S, E))

	ttk.Label(insert_frame, text="What is the name of the first component in the circuit involved in the connection?").grid(column=1, row=1, sticky=W)

	component_1_name = ttk.Combobox(insert_frame)
	component_1_name['values'] = tuple(name_dict.keys())
	component_1_name.grid(column=1, row=2, sticky=W)

	ttk.Label(insert_frame, text="   On what pin number?").grid(column=2, row=1, sticky=W)

	pin_1 = ttk.Entry(insert_frame)
	pin_1.grid(column=2, row=2, sticky=W)

	ttk.Label(insert_frame, text="What is the name of the second component in the circuit involved in the connection?").grid(column=1, row=3, sticky=W)

	component_2_name = ttk.Combobox(insert_frame)
	component_2_name['values'] = tuple(name_dict.keys())
	component_2_name.grid(column=1, row=4, sticky=W)

	ttk.Label(insert_frame, text="   On what pin number?").grid(column=2, row=3, sticky=W)

	pin_2 = ttk.Entry(insert_frame)
	pin_2.grid(column=2, row=4, sticky=W)

	def insert_button():
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
					FYI("New connections made! Check the terminal window for an updated list.")
			except ValueError:
				warning("Sorry, check that your pin numbers exist and are actually numbers!")

	ttk.Button(insert_frame, text="Make connection!", command = insert_button).grid(column=1, row=5, sticky=W)
	ttk.Button(insert_frame, text="Back", command=lambda: insert_window.destroy()).grid(column=2, row=5, sticky=W)


def GUI_remove(*args):
	pass

def GUI_connections(*args):
	print_connections_helper()
	FYI("A list of connections currently in the circuit has been printed to the terminal screen.")


def GUI_components(*args):
	print_components_helper()
	FYI("A list of components currently in the circuit has been printed to the terminal screen.")

def GUI_quit(*args):
	root.destroy()
	exit(0)

def warning(inmessage):
	messagebox.showinfo(message=inmessage, icon='error', title="Uh-oh...")

def FYI(inmessage):
	messagebox.showinfo(message=inmessage, icon='info', title="FYI...")

def print_connections_helper():
	os.system('cls' if os.name=='nt' else 'clear')
	print ("Current list of all connections in circuit:")
	print ("")
	da_circuit.print_connections()
	print ("")
	print ("End of list.")

def print_components_helper():
	os.system('cls' if os.name=='nt' else 'clear')
	print("Current list of all components in the circuit...")
	print ("")
	for part in name_dict:
			print (part + " is a " + name_dict[part][0])
	print ("")
	print ("End of list.")


ttk.Label(mainframe, text="Welcome to JustBreadBoardIt! What will you do?").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Add component to circuit", command=GUI_add).grid(column=1, row = 2, sticky=W)
ttk.Button(mainframe, text="Connect two components in circuit", command=GUI_insert).grid(column=2, row = 2, sticky=W)
ttk.Button(mainframe, text="Remove a connection", command=GUI_remove).grid(column=3, row = 2, sticky=W)
ttk.Button(mainframe, text="Print components in circuit", command=GUI_components).grid(column=1, row = 3, sticky=W)
ttk.Button(mainframe, text="Print connections in circuit", command=GUI_connections).grid(column=2, row = 3, sticky=W)
ttk.Button(mainframe, text="Quit program", command=GUI_quit).grid(column=3, row = 3, sticky=W)


root.mainloop()









"""
NOTE: This is some test code to scaffold the structure of the GUI code. 

def button_test(*args):
	print ("You pushed the button!")

def window(*args):

	def back(*args):
		new_window.destroy()


	new_window = Toplevel(root)
	new_frame = ttk.Frame(new_window, padding="3 3 12 12")
	new_frame.grid(column=0, row=0, sticky=(N, W, S, E))

	

	ttk.Button(new_frame, text="Push me!", command=button_test).grid(column=1, row=1, sticky=W)
	ttk.Button(new_frame, text="Back", command=back).grid(column=2, row=1, sticky=W)


ttk.Label(mainframe, text='TEST').grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Push me!", command=window).grid(column=1, row=2, sticky=W) 
"""