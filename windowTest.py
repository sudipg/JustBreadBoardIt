from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text ="error", relief=RAISED,\
                         bitmap="error")
B2 = tkinter.Button(top, text ="hourglass", relief=RAISED,\
                         bitmap="hourglass")
B3 = tkinter.Button(top, text ="info", relief=RAISED,\
                         bitmap="info")
B4 = tkinter.Button(top, text ="question", relief=RAISED,\
                         bitmap="question")
B5 = tkinter.Button(top, text ="warning", relief=RAISED,\
                         bitmap="warning")
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
