from tkinter import *

root = Tk()

button_01 = Button(root, text="Button 01")
button_01.grid(row=1, column=1, padx=5, pady=5)


button_02 = Button(root, text="Button 02")
button_02.grid(row=1, column=2, padx=5, pady=5)

button_03 = Button(root, text="Button 03")
button_03.grid(row=2, column=1, padx=5, pady=5)


button_04 = Button(root, text="Button 04")
button_04.grid(row=2, column=2, padx=5, pady=5)


button_05 = Button(root, text="Button 05")
button_05.grid(row=3, column=1, padx=5, pady=5)


button_06 = Button(root, text="Button 06")
button_06.grid(row=3, column=2, padx=5, pady=5)

button_07 = Button(root, text="Button 07")
button_07.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()