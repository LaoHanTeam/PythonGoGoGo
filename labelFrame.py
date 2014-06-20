from Tkinter import *

root = Tk()

labelframe = LabelFrame(root, text="This is a labelFrame")
labelframe.pack(fill="both",expand="yes")

left = Label(labelframe, text = "Inside the labelFrame")
left.pack()

root.mainloop()
