from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, expand=YES, fill=BOTH)

button_01 = Button(topFrame, text="Button 01")
button_01.pack(side=LEFT)

button_02 = Button(topFrame, text="Button 02")
button_02.pack(side=LEFT)

button_03 = Button(topFrame, text="Button 03")
button_03.pack(side=LEFT)

button_04 = Button(bottomFrame, text="Button 04")
button_04.pack(side=BOTTOM, expand=YES, fill=X)

root.mainloop()

