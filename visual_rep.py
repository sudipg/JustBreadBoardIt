from tkinter import *
from tkinter import ttk

class Visual_rep(object):

	def __init__(self, parent):
		self.root = Toplevel(parent)
		self.canvas = Canvas(self.root, width=2000, height=250)
		self.canvas.pack()
		self.minimum_x = 0


		self.connections = []
		self.components = {}



	def insert(self, label, length, height):

		self.components[label] = {}
		pins = self.components[label]

		pin_number = 1

		self.canvas.create_text((length*12)/2 + self.minimum_x, 10, anchor=W, font="Purisa", text=label)

		h_countdown = height
		
		local_top_y = 20
		local_bottom_y = 30
		
		while (h_countdown > 0):
			l_countdown = length
			
			local_top_x = self.minimum_x
			local_bottom_x = self.minimum_x + 10
			while (l_countdown > 0):
				pins[pin_number] = ((local_top_x + local_bottom_x)/2, (local_top_y + local_bottom_y)/2)
				self.canvas.create_rectangle(local_top_x, local_top_y, local_bottom_x, local_bottom_y, fill='blue')
				local_top_x += 20
				local_bottom_x += 20
				l_countdown -= 1
				pin_number += 1
			local_top_y += 20
			local_bottom_y += 20
			h_countdown -= 1

		self.minimum_x += length*20 + 50

	def connect(self, component_1, pin_1, component_2, pin_2):
		x1 = self.components[component_1][pin_1][0]
		y1 = self.components[component_1][pin_1][1]

		x2 = self.components[component_2][pin_2][0]
		y2 = self.components[component_2][pin_2][1]

		id = self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

		self.connections.append((component_1, component_2, id))


	def remove(self, component_1, pin_1, component_2, pin_2):
		
		for x in self.connections:
			if (x[0] == component_1 and x[1] == component_2) or (x[0] == component_2 and x[1] == component_1):
				print (x[1])
				self.canvas.delete(x[2])
				pointer = x
		self.connections.remove(pointer)

		
'''
test = Visual()
test.insert("Hi!", 4, 5)
test.insert("Lawl", 3, 3)
test.insert("Yay", 2, 2)
test.insert("Yeesh", 5, 5)
test.insert("Resistor 1", 2, 2)
test.insert("Resistor 2", 2, 2)
test.insert("Jimmy", 4, 4)
test.insert("Carol", 5, 2)

test.connect("Lawl", 8, "Yay", 3)
test.connect("Hi!", 3, "Yeesh", 7)

test.remove("Lawl", 8, "Yay", 3)
'''



"""
root = Tk()

w = Canvas(root, width=2000, height=100)
w.pack()


w.create_text(10, 10, anchor=W, font="Purisa", text="This is a test!")
w.create_rectangle(20, 20, 30, 30, fill="blue")
w.create_rectangle(40, 20, 50, 30, fill="blue")

w.create_rectangle(20, 40, 30, 50, fill="blue")
"""

