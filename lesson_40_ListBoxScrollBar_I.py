from tkinter import *

root = Tk()

def onselect(event):

    myW = event.widget
    index = int(myW.curselection()[0])
    value = myW.get(index)
    print("You selected item %d: %s" % (index,value))


myScrollBar = Scrollbar(root)
myScrollBar.pack(side=RIGHT, fill=Y)

myListBox = Listbox(root, yscrollcommand=myScrollBar)

for item in range(200):
    myListBox.insert(END, "Item " + str(item))


myListBox.pack(side=LEFT, fill=BOTH)
myListBox.bind("<<ListboxSelect>>", onselect)

myScrollBar.config(command=myListBox.yview)

root.mainloop()


