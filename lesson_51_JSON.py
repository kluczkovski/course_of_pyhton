from tkinter import *
import json

class App:

    def __init__(self, master):
        master.geometry("600x100")
        master.title("Json Example: Read/Write")
        myframe = Frame(master)
        myframe.pack()

        btSave = Button(myframe, text="Save JSON File", command=self.saveJSON)
        btSave.pack(side=LEFT)

        btRead = Button(myframe, text="Read JSON File", command=self.readJSON)
        btRead.pack(side=LEFT)

        #ID
        idFrame = Frame(master)
        idFrame.pack(side=LEFT, pady=10)
        self.idLabel = Label(idFrame, text="ID:")
        self.idLabel.pack(side=LEFT)
        self.idEntry = Entry(idFrame)
        self.idEntry.pack(side=LEFT)

        #Name
        nameFrame = Frame(master)
        nameFrame.pack(side=LEFT, pady=10)
        self.nameLabel = Label(nameFrame, text="Name:")
        self.nameLabel.pack(side=LEFT)
        self.nameEntry = Entry(nameFrame)
        self.nameEntry.pack(side=LEFT)

        #City
        cityFrame = Frame(master)
        cityFrame.pack(side=LEFT, pady=10)
        self.cityLabel = Label(cityFrame, text='City:')
        self.cityLabel.pack(side=LEFT)
        self.cityEntry = Entry(cityFrame)
        self.cityEntry.pack(side=LEFT)



    def saveJSON(self):

        data = {'id': self.idEntry.get(), 'name' : self.nameEntry.get(), 'city' : self.cityEntry.get()}
        with open ("myFile.json", "w") as myFileJSON:
            json.dump(data, myFileJSON)


    def readJSON(self):

        with open ("myFile.json", "r") as myFile:
            data = json.load(myFile)
            self.idEntry.insert(INSERT, data['id'])
            self.nameEntry.insert(INSERT, data['name'])
            self.cityEntry.insert(INSERT, data['city'])


root = Tk()
app = App(root)
root.mainloop()


