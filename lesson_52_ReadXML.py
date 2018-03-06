import xml.etree.ElementTree as ET
import os.path
from tkinter import *


global_customer_count = 0

class App:

    def __init__(self, master):

        master.geometry("300x150")
        master.title("Read XML file")
        frame = Frame(master)
        frame.pack()

        buttonRead = Button(frame, text='Read Element in XML File', command=self.readXML)
        buttonRead.pack(side=LEFT)

        self.countLabel = Label(frame)
        self.countLabel.pack(side=LEFT)

        # Name
        nameFrame = Frame(master)
        nameFrame.pack(side=BOTTOM, pady=10)
        self.nameLabel = Label(nameFrame, text='Text: ')
        self.nameLabel.pack(side=LEFT, padx=5)
        self.nameEntry = Entry(nameFrame)
        self.nameEntry.pack(side=LEFT, padx=5)

        # Id
        idFrame = Frame(master)
        idFrame.pack(side=BOTTOM, pady=10)
        self.idLabel = Label(idFrame, text='Id: ')
        self.idLabel.pack(side=LEFT, padx=5)
        self.idEntry = Entry(idFrame)
        self.idEntry.pack(side=LEFT, padx=5)

    def readXML(self):

        fileName = "customers.xml"

        if os.path.isfile(fileName):

            global global_customer_count

            tree = ET.parse(fileName)
            root = tree.getroot()

            self.idEntry.delete(0, 'end')
            self.nameEntry.delete(0, 'end')
            self.idEntry.insert(INSERT, str(root[global_customer_count][0].text))
            self.nameEntry.insert(INSERT, str(root[global_customer_count][1].text))

            count = 0
            for customer in root.iter('customer'):
                count += 1

            self.countLabel.configure(text=str(global_customer_count + 1) + " / " + str(count))

            global_customer_count +=1
        else:
            print("File not found")


root = Tk()
app = App(root)
root.mainloop()