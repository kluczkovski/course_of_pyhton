from lxml import etree
from tkinter import *
import os.path

class App:

    def __init__(self, master):

        master.geometry("300x100")
        master.title("XML Validation")
        frame = Frame(master)
        frame.pack()

        self.btValidate = Button(frame, text="Validation XML File", command=self.validadeXML)
        self.btValidate.pack(side=LEFT)

        frameLabel = Frame(master)
        frameLabel.pack(side=BOTTOM, pady=10, expand=TRUE, fill=BOTH)

        self.labelValidation = Label(frameLabel)
        self.labelValidation.pack(side=LEFT, expand=TRUE, fill=BOTH)


    def validadeXML(self):

        try:
            XMLfileName = "customers.xml"
            XSDfileName = "validate_customers.xsd"

            if os.path.isfile(XMLfileName) and os.path.isfile(XSDfileName):

                xmlschema_doc = etree.parse(XSDfileName)
                xmlschema = etree.XMLSchema(xmlschema_doc)

                xml_file = etree.parse(XMLfileName)
                if xmlschema.validate(xml_file):
                    self.labelValidation.configure(text="XML is Validate")
                else:
                    self.labelValidation.configure(text="XML is NOT Validate I")
            else:
                print("Files not exist")

        except etree.XMLSyntaxError:
            self.labelValidation.configure(text="XML ERROR")

        except etree.DocumentInvalid:
            self.labelValidation.configure(text="XML is NOT Validate")


root = Tk()
app = App(root)
root.mainloop()
