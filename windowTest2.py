#Displays a circle bouncing around the canvas window.
from tkinter import *

window = Tk()
canvas = Canvas(window, width = window.winfo_screenwidth(), height = window.winfo_screenheight())
canvas.pack()

x0 = 10		# initial left-most edge of ball
y0 = 50		# initial top-most edge of ball
x1 = 60		# inital right-most edge of ball
y1 = 100	# you've probably got the idea by now.
dx = 2
dy = 3

# create ball:
which = canvas.create_oval(x0,y0,x1,y1,fill="blue", tag='blueBall')

while True:
    canvas.move('blueBall', dx, dy)

    canvas.height = window.winfo_height()
    canvas.width = window.winfo_width()
    canvas.after(20)

    canvas.update()
# the next 4 if statements check if the ball hits a wall: if it hits
# a floor/ceiling its y-velocity reverses and it if hits a left/right 
# wall its x-velocity reverses
    if x1 >= window.winfo_width():
        dx = -2
    if x0 <= 0:
        dx = 2
    if y0 < 0:
        dy = 3
    if y1 >= window.winfo_height():
        dy = -3


    x0 += dx
    x1 += dx
    y0 += dy
    y1 += dy

window.mainloop()
