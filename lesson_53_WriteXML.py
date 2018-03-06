import xml.etree.ElementTree as ET
import os.path
from tkinter import *

class App:

    def __init__(self, master):
        master.geometry("300x150")
        master.title("Write XML")
        frame = Frame(master)
        frame.pack()

        btSave = Button(frame, text="Save XML", command=self.saveXML)
        btSave.pack(side=LEFT)

        nameFrame = Frame(master)
        nameFrame.pack(side=BOTTOM, pady=10)
        self.nameLabel = Label(nameFrame, text="Name:")
        self.nameLabel.pack(side=LEFT, padx=5)
        self.nameEntry = Entry(nameFrame)
        self.nameEntry.pack(side=LEFT, padx=5)

        idFrame = Frame(master)
        idFrame.pack(side=BOTTOM, pady=10)
        self.idLabel = Label(idFrame, text="Id:")
        self.idLabel.pack(side=LEFT, padx=5)
        self.idEntry = Entry(idFrame)
        self.idEntry.pack(side=LEFT, padx=5)

    def saveXML(self):

        fileName = "customers.xml"
        if os.path.isfile(fileName):   #Already exist

            tree = ET.parse(fileName)
            root = tree.getroot()

            doc = ET.SubElement(root, "customer")
            ET.SubElement(doc, "id").text = str(self.idEntry.get())
            ET.SubElement(doc, "name").text = str(self.nameEntry.get())

            saveTree = ET.ElementTree(root)
            saveTree.write(fileName)

        else:
            root = ET.Element("root")
            doc  = ET.SubElement(root, "customer")
            ET.SubElement(doc, "id").text = str(self.idEntry.get())
            ET.SubElement(doc, "name").text = str(self.nameEntry.get())

            saveTree = ET.ElementTree(root)
            saveTree.write(fileName)



root = Tk()
app = App(root)
root.mainloop()