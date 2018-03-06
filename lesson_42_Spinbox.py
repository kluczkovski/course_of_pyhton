from tkinter import *

root = Tk()

def showValue():
    selection = "Value is spinbox is " + str(mySpinBox.get())
    myLabel.configure(text=selection, font="Arial 20", fg="blue")



#mySpinBox = Spinbox(root, from_=0, to=10, command=showValue)
mySpinBox = Spinbox(root, values=('Green', 'Red', 'Blue', 'Yellow'), command=showValue)
mySpinBox.pack()

myLabel = Label(root)
myLabel.pack(padx=20, pady=20)




root.mainloop()