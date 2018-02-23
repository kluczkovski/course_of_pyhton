from tkinter import *

root = Tk()

myButton = Button(root, text="My Button")
myButton.pack()

myButton.place(bordermode=OUTSIDE, heigh=30, width=100, x=10, y=50)


root.mainloop()