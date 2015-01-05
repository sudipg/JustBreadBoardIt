from tkinter import *
from tkinter import ttk
from visual_rep import Visual_rep

import circuit

## ** Init GUI

root = Tk()
root.title("JustBreadBoardIt!")
root.attributes('-zoomed', True)

circuit_window = PanedWindow(master=root, borderwidth=5, sashwidth=5, bg="#fff")
circuit_window.pack(fill=BOTH, expand=1)

circuit_frame = Frame(circuit_window)
circuit_window.add(circuit_frame)

workspace_window = PanedWindow(circuit_window, orient=VERTICAL, sashwidth=5, bg="#fff")
circuit_window.add(workspace_window)

command_frame = Frame(workspace_window)
workspace_window.add(command_frame)

console_frame = Frame(workspace_window)
workspace_window.add(console_frame)

text_widget = Text(console_frame, state=DISABLED)
text_widget.pack()

## ** Init Circuit
component_dict = {'resistor' : circuit.Resistor, 'capacitor' : circuit.Capacitor, 'positive_battery' : circuit.Battery_positive, 'negative_battery' : circuit.Battery_negative, 'led' : circuit.LED, 'button' : circuit.Button, 'switchboard': circuit.Switchboard}
circuit = circuit.Circuit()
vis_rep = Visual_rep(circuit_frame);
name_dict = {}

## ** Helper Functions

def print_to_console(string):
  text_widget.config(state=NORMAL)
  text_widget.insert(INSERT, string)
  text_widget.config(state=DISABLED)

def print_components_helper():
  string = "Current list of components: \n"
  for part in name_dict:
    string += '\t* ' + str(part) + " is a " + str(name_dict[part][0]) + '\n'
  print_to_console(string)

def print_connections_helper():
  string = "Current list of connections: \n"
  string += circuit.get_connections()
  print_to_console(string)

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

  holder_function = lambda: command_function(component_1_name, pin_1, component_2_name, pin_2)
  ttk.Button(insert_frame, text=button_text, command = holder_function).grid(column=1, row=5, sticky=W)

## ** GUI Function

def GUI_add(*args):
  print_components_helper()

  add_window = Toplevel(root)
  add_frame = ttk.Frame(add_window, padding="3 3 12 12")
  add_frame.grid(column=0, row=0, sticky=(N, W, S, E))

  ttk.Label(add_frame, text="What kind of component would you like to add?").grid(column=1, row=1, sticky=W)
      
  component_type = ttk.Combobox(add_frame)
  component_type.grid(column=1, row=2, sticky=W)
  component_type['values'] =  ('resistor', 'capacitor', 'positive_battery', 'negative_battery', 'led', 'button', 'switchboard')
  component_type.set('resistor')

  ttk.Label(add_frame, text="What will it be called?").grid(column=1, row=3, sticky=W)

  component_name = ttk.Entry(add_frame)
  component_name.grid(column=1, row = 4, sticky=W)

  #A function called when the user hits the final button.
  def add_button():
    if component_name.get() == '':
      print_to_console("Whoah there tiger, looks like you forget a name there!")
    elif component_name.get() in name_dict:
      print_to_console("Sorry, looks like there's a part with that name already in the circuit.")
    else:
      component_reference = component_dict[component_type.get()](component_name.get())
      circuit.insert_component(component_reference)
      name_dict[component_name.get()] = [component_type.get(), component_reference]
      da_rep.insert(component_name.get(), component_type.get(), component_reference.x_length, component_reference.y_length)
      print_components_helper()
      print_to_console("Successfully added a " + component_type.get() + " named " + component_name.get())
    ttk.Button(add_frame, text="Add part!", command=add_button).grid(column=1, row=5, sticky=W)
    ttk.Button(add_frame, text="Back", command= lambda: add_window.destroy()).grid(column=2, row=5, sticky = W)

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
             print_to_console("Sorry, that connection already exists!") 
           elif tester == 3:
             print_to_console("Sorry, looks like you're trying to conenct pins that don't exist!") 
         else:
           da_rep.connect(component_1_name.get(), int(pin_1.get()), component_2_name.get(), int(pin_2.get()))
           print_to_console("New connections made! Check the terminal window for an updated list.")
       except ValueError:
         print_to_console("Sorry, check that your pin numbers exist and are actually numbers!")
  insert_helper("involved in the new connection", "Make connection!", insert_button)

def GUI_remove(*args):
  def remove_button(component_1_name, pin_1, component_2_name, pin_2):
    if component_1_name.get() == '' or component_2_name.get() == '':
      warning("Oops..looks like you forgot a component name there!")
    else:
      try:
        tester = da_circuit.remove_connection(name_dict[component_1_name.get()][1], int(pin_1.get()), name_dict[component_2_name.get()][1], int(pin_2.get()))
        print_connections_helper()
        if tester == 1:
          rep.remove(component_1_name.get(), int(pin_1.get()), component_2_name.get(), int(pin_2.get()))
          print_to_console("Connection successfully removed. Please check the terminal window for an updated list of connections.")
        elif tester == 2:
          print_to_console("Whoops! You're trying to remove a connection that doesn't exist.")	
      except ValueError:
        print_to_console("Sorry, check that your pin numbers exist and are actually numbers!")
  insert_helper("involved in the removed connection", "Remove connection!", remove_button)

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

## ** Adding GUI functions
ttk.Label(command_frame, text="Welcome to JustBreadBoardIt! What will you do?").grid(column=1, row=1, sticky=W)
ttk.Button(command_frame, text="Add component to circuit", command=GUI_add).grid(column=1, row = 2, sticky=W)
ttk.Button(command_frame, text="Connect two components in circuit", command=GUI_insert).grid(column=2, row = 2, sticky=W)
ttk.Button(command_frame, text="Remove a connection", command=GUI_remove).grid(column=3, row = 2, sticky=W)
ttk.Button(command_frame, text="Print components in circuit", command=GUI_components).grid(column=1, row = 3, sticky=W)
ttk.Button(command_frame, text="Print connections in circuit", command=GUI_connections).grid(column=2, row = 3, sticky=W)
ttk.Button(command_frame, text="Quit program", command=GUI_quit).grid(column=3, row = 3, sticky=W)

## ** Main loop
root.mainloop()
