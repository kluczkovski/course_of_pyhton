from tkinter import *

class App():

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.buttonQuit = Button(frame, text="Quit", fg="red", command=self.quit)
        self.buttonQuit.pack(side=LEFT)

        self.buttonHello = Button(frame, text="Hello", command=self.hello)
        self.buttonHello.pack(side=LEFT)

    def quit(self):
        root.destroy()

    def hello(self):
        print("Hello Python")


root = Tk()
app = App(root)
root.mainloop()