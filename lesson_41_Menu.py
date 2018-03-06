from tkinter import *

class MyAppUI(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("My App")
        self.master.geometry("400x130")

        self.menuBar = Menu(self)

        self.fileMenu = Menu(self)
        self.editMenu = Menu(self)
        self.colorMenu = Menu(self)
        self.sizeMenu = Menu(self)

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Quit", command=self.quit)

        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
        self.editMenu.add_cascade(label="Color", menu=self.colorMenu)
        self.colorMenu.add_command(label="Red", command=self.colorRed)
        self.colorMenu.add_command(label="Green", command=self.colorGreen)
        self.colorMenu.add_command(label="Blue", command=self.colorBlue)


        self.editMenu.add_cascade(label="Size", menu=self.sizeMenu)
        self.sizeMenu.add_command(label="Arial 10", command=self.size10)
        self.sizeMenu.add_command(label="Arial 30", command=self.size30)
        self.sizeMenu.add_command(label="Arial 50", command=self.size50)



        self.master.config(menu=self.menuBar)



        self.Frame_01 = Frame(self)
        self.Frame_01.pack()

        self.label_01 = Label(self.Frame_01, fg="Black", text="Clara Kluczkovski", font="Arial 30")
        self.label_01.pack(side=LEFT, pady=20)


    def quit(self):
        self.master.destroy()

    def colorRed(self):
        self.label_01.configure(fg="Red")

    def colorGreen(self):
        self.label_01.configure(fg="Green")

    def colorBlue(self):
        self.label_01.configure(fg="Blue")

    def size10(self):
        self.label_01.configure(font="Arial 10")

    def size30(self):
        self.label_01.configure(font="Arial 30")

    def size50(self):
        self.label_01.configure(font="Arial 50")


root = Tk()

app = MyAppUI()
app.pack()

root.mainloop()

