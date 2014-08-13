from tkinter import *
from tkinter import ttk

root = Tk()

w = Canvas(root, width=2000, height=100)
w.pack()


w.create_text(10, 10, anchor=W, font="Purisa", text="This is a test!")
w.create_rectangle(20, 20, 30, 30, fill="blue")
w.create_rectangle(40, 20, 50, 30, fill="blue")

w.create_rectangle(20, 40, 30, 50, fill="blue")

mainloop()