from tkinter import *

class App(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Demo of radionButton, checkbutton and button with image")
        self.master.geometry("400x100")

        # Frame 01
        self.frame_01 = Frame(self)
        self.frame_01.pack()

        self.text = Entry(self.frame_01, width=40, font="Arial 10")
        self.text.insert(INSERT, "Lorem ipsum dolor site amet.")
        self.text.pack(padx=5, pady=5)


        # Frame 02
        self.frame_02 = Frame(self)
        self.frame_02.pack()

        self.chosenColor = StringVar()
        self.chosenColor.set(0)

        self.radioRed = Radiobutton(self.frame_02, text="Red", variable=self.chosenColor, value="red",
                                    command=self.changeColor)
        self.radioRed.pack(side=LEFT, padx=5, pady=5)

        self.radioBlue = Radiobutton(self.frame_02, text="Blue", variable=self.chosenColor, value="blue",
                                     command=self.changeColor)
        self.radioBlue.pack(side=LEFT, padx=5, pady=5)

        self.radioGreen = Radiobutton(self.frame_02, text="Green", variable=self.chosenColor, value="green",
                                      command=self.changeColor)
        self.radioGreen.pack(side=LEFT, padx=5, pady=5)


        # Frame 3
        self.frame_03 = Frame(self)
        self.frame_03.pack()

        self.boldOn = BooleanVar()
        self.checkBold = Checkbutton(self.frame_03, text="Bold", variable=self.boldOn, command=self.changeFont)
        self.checkBold.pack(side=LEFT, padx=5, pady=5)

        self.italicOn = BooleanVar()
        self.checkItalic = Checkbutton(self.frame_03, text="Italic", variable= self.italicOn, command=self.changeFont)
        self.checkItalic.pack(side=LEFT, padx=5, pady=5)


        # Frame 4
        self.frame_04 = Frame(self)
        self.frame_04.pack()

        self.myImage = PhotoImage(file="nirvana.gif")
        self.clearButton = Button(self.frame_04, image=self.myImage, command=self.clearText)
        self.clearButton.pack(side=LEFT, padx=5, pady=5)





    def changeColor(self):
        if self.chosenColor.get() == "red":
            self.text.configure(fg="red")
        elif self.chosenColor.get() == "blue":
            self.text.configure(fg="blue")
        elif self.chosenColor.get() == "green":
            self.text.configure(fg="Green")

    def changeFont(self):
        desireFont = "Arial 10"

        if self.boldOn.get():
            desireFont += " bold"

        if self.italicOn.get():
            desireFont += " italic"

        self.text.configure(font=desireFont)

    def clearText(self):
        self.text.delete(0, END)

def main():
    App().mainloop()


if __name__ == "__main__":
    main()
