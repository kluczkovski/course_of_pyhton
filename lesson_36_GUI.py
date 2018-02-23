from tkinter import *
from tkinter import messagebox

class EntryDemo(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("My rectangle area calculator")
        self.master.geometry("400x100")
        self.configure(background="#F8FBEF")

        # Frame 01
        self.frame_01 = Frame(self)
        self.frame_01.pack(pady=5)

        self.label_01 = Label(self.frame_01, fg="blue", bg="yellow", text="Size 1:")
        self.label_01.pack(side=LEFT, padx=5)

        self.text_01 = Entry(self.frame_01, width=17, name="number1")
        self.text_01.insert(INSERT, "Enter size of side 1")
        self.text_01.pack(side=LEFT, padx=5)


        # Frame 02
        self.frame_02 = Frame(self)
        self.frame_02.pack(pady=5)

        self.label_02 = Label(self.frame_02, fg="red", bg="black", text="Size 2:")
        self.label_02.pack(side=LEFT, padx=5)

        self.text_02 = Entry(self.frame_02, width=17, name="number2")
        self.text_02.insert(INSERT, "Enter size of side 2")
        self.text_02.pack(side=LEFT, padx=5)


        # Frame 03
        self.frame_03 = Frame(self)
        self.frame_03.pack(pady=5)

        self.button_01 = Button (self.frame_03, text="Quit", command=self.quit)
        self.button_01.pack(side=LEFT, padx=5)

        self.button_02 = Button(self.frame_03, text="Calculate", command=self.calculateArea)
        self.button_02.pack(side=LEFT, padx=5)

    def quit(self):
        self.master.destroy()


    def calculateArea(self):
        area = int(self.text_01.get()) * int(self.text_02.get())
        messagebox.showinfo("Result", "The area is: " + str(area))



def main():
    EntryDemo().mainloop()



if __name__ == "__main__":
    main()
