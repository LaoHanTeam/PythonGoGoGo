from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)


redbutton.pack(side = LEFT)

greenbutton = Button(frame,text="Brown" , fg="brown")
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text="Blue" , fg="blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe,text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

root.mainloop()