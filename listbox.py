from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1,"Python")
Lb1.insert(2,"Perl")
Lb1.insert(3,"C")
Lb1.pack()

top.mainloop()
