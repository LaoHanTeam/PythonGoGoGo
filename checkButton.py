from Tkinter import *
import tkMessageBox
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

def chgValueCmd():
    tkMessageBox.showinfo("text","your change the button's state")


C1 = Checkbutton(top,text = "Music" , variable=CheckVar1, onvalue = 1 , offvalue = 0, height = 5 , width = 20 , command = chgValueCmd)

C2 = Checkbutton(top,text = "Video" , variable=CheckVar2, onvalue = 1 , offvalue = 0, height = 5 , width = 20)

C1.pack()
C2.pack()

top.mainloop()
