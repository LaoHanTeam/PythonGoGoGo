#!/usr/bin/python

from Tkinter import * 
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def callbackCmd():
    print "hello world "
    tkMessageBox.showinfo("hello","hello , this is a callback")


B1 = Tkinter.Button(top,text="FLAT" , relief=FLAT , activebackground="red" , bg="blue",command=callbackCmd)
B2 = Tkinter.Button(top,text="RAISED", relief = RAISED)
B3 = Tkinter.Button(top,text="SUNKEN",relief = SUNKEN)
B4 = Tkinter.Button(top,text="GROOVE",relief = GROOVE)
B5 = Tkinter.Button(top,text="RIDGE",relief = RIDGE)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
