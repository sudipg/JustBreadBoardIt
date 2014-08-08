import os
from tkinter import *
from tkinter import ttk
import circuit

os.system('cls' if os.name=='nt' else 'clear')
print('YUP!')

da_circuit = circuit.Circuit()
name_dict = {}

root = Tk()

root.title("JustBreadBoardIt!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))


def GUI_add(*args):
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
			warning(add_window, "Whoah there tiger, looks like you forget a name there!")
		elif component_name.get() in name_dict:
			warning(add_window, "Sorry, looks like there's a part with that name already in the circuit.")
		else:
			component_reference = component_dict[component_type.get()](component_name.get())
			da_circuit.insert_component(component_reference)
			name_dict[component_name.get()] = [component_type.get(), component_reference]
			warning(add_window, "Successfully added a " + component_type.get() + " named " + component_name.get() + " !")
			
	ttk.Button(add_frame, text="Add part!", command=add_button).grid(column=1, row=5, sticky=W)
	ttk.Button(add_frame, text="Back", command= lambda: add_window.destroy()).grid(column=2, row=5, sticky = W)


def GUI_insert(*args):

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




def GUI_remove(*args):
	pass

def GUI_connections(*args):
	pass

def GUI_components(*args):
	return
	da_circuit.print_components()

def GUI_quit(*args):
	root.destroy()
	exit(0)

def warning(window, message):
	warning_window = Toplevel(window)
	warning_frame = ttk.Frame(warning_window, padding="3 3 12 12")
	warning_frame.grid(column=0, row=0, sticky=(N, W, S, E))
	ttk.Label(warning_frame, text=message).grid(column=1, row=1, sticky=W)
	ttk.Button(warning_frame, text='OK', command = lambda: warning_window.destroy()).grid(column=1, row=2, sticky=W)



	







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