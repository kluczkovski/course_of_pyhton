from tkinter import *

root = Tk()

myListBox = Listbox(root)
myListBox.insert("1", "Red")
myListBox.insert("2", "Green")
myListBox.insert("3", "Blue")
myListBox.insert("4", "Yellow")
myListBox.insert("5", "Black")
myListBox.insert("1", "Pink")


myListBox.pack()



root.mainloop()