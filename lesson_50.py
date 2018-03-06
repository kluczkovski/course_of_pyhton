from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import *

class App:

    def __init__(self, master):
        master.geometry("300x300")
        master.title("My Read/Write File Example")
        frame = Frame(master)
        frame.pack()

        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM, expand=YES, fill=BOTH)

        self.buttonRead = Button(frame, text="Read File", command=self.readFile)
        self.buttonRead.pack(side=LEFT)

        self.buttonSave = Button(frame, text="Save File", command=self.saveFile)
        self.buttonSave.pack(side=LEFT)

        self.showText = ScrolledText(bottomFrame)
        self.showText.pack(side=LEFT, padx=5, expand=YES, fill=BOTH)


    def readFile(self):

        # Second Implementation
        myFile = askopenfile(parent=root, mode="rb", title="Select File")
        if myFile != None:
            data = myFile.read()
            self.showText.insert("1.0", data)
            myFile.close()

        # First Implementation
        #with open("myFile.txt", "r") as myFile:
        #    for line in myFile:
        #        self.showText.insert(END, line)


    def saveFile(self):

        # Second Implementation
        myFile = asksaveasfile(mode="w")
        if myFile != None:
            data = self.showText.get("1.0", END+"-1c")
            myFile.write(data)
            myFile.close()


        # First implementation
        #myFile = open("myFile.txt", "w")
        #data = self.showText.get("1.0", END+"-1c")
        #data = self.showText.get("1.00", END)
        #myFile.write(data)
        #myFile.close()



root = Tk()
app = App(root)
root.mainloop()