from tkinter import *


def showSelection():
    selection = "Value = " + str(var.get())
    myLabel.configure(text=selection)


root = Tk()

var = DoubleVar()

myScale = Scale(root, length=300, variable=var, from_=0, to=1000, resolution=10, tickinterval=100)
myScale.pack(anchor=CENTER)

myButton = Button(root, text="Show Selected in the Scale", command=showSelection)
myButton.pack(anchor=CENTER, pady=20, padx=20)

myLabel = Label(root)
myLabel.pack()

root.mainloop()



