import os
from tkinter import *
from tkinter import ttk

os.system('cls' if os.name=='nt' else 'clear')
print('YUP!')

root = Tk()

root.title("JustBreadBoardIt!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, S, E))

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

def GUI_add(*args):
	pass

def GUI_insert(*args):
	pass

def GUI_remove(*args):
	pass

def GUI_connections(*args):
	pass

def GUI_components(*args):
	pass

def GUI_quit(*args):
	root.destroy()
	exit(0)

ttk.Label(mainframe, text="Welcome to JustBreadBoardIt! What will you do?").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Add component to circuit", command=GUI_add).grid(column=1, row = 2, sticky=W)
ttk.Button(mainframe, text="Connect two components in circuit", command=GUI_insert).grid(column=2, row = 2, sticky=W)
ttk.Button(mainframe, text="Remove a connection", command=GUI_remove).grid(column=3, row = 2, sticky=W)
ttk.Button(mainframe, text="Print components in circuit", command=GUI_components).grid(column=1, row = 3, sticky=W)
ttk.Button(mainframe, text="Print connections in circuit", command=GUI_connections).grid(column=2, row = 3, sticky=W)
ttk.Button(mainframe, text="Quit program", command=GUI_quit).grid(column=3, row = 3, sticky=W)


root.mainloop()