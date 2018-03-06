from tkinter import *
import pymysql



def whichSelected():
    if len(listProduct.curselection()) > 0:
        #return str(listProduct.curselection()[0] + 1)
        return listProduct.get(listProduct.curselection())

def loadEntry():

    item = whichSelected()
    if (item is not None):

        #Get information from database
        db = pymysql.connect("localhost", "root", "everton", "guessBook")
        cursor = db.cursor()
        sql = "select * from tbproducts where product='%s'" %item
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row)

        #new screen
        windowsLoad = Toplevel()
        windowsLoad.title("Product:")

        frame = Frame(windowsLoad)
        frame.pack()

        #ID
        idLabel = Label(frame, text="Id:")
        idLabel.grid(row=0, column=0, sticky=W)
        idVar = StringVar()
        idVar.set(row[0])
        idEntry = Entry(frame, textvariable=idVar, state=DISABLED)
        idEntry.grid(row=0, column=1, sticky=W)

        #Product
        productLabel = Label(frame, text="Product:")
        productLabel.grid(row=1, column=0, sticky=W)
        productVar = StringVar()
        productVar.set(row[1])
        productEntry = Entry(frame, textvariable=productVar, state=DISABLED)
        productEntry.grid(row=1, column=1, sticky=W)

        # Description
        dscLabel = Label(frame, text="Description:")
        dscLabel.grid(row=2, column=0, sticky=W)
        dscVar = StringVar()
        dscVar.set(row[2])
        dscEntry = Entry(frame, textvariable=dscVar, state=DISABLED)
        dscEntry.grid(row=2, column=1, sticky=W)

        # Quantity
        quantityLabel = Label(frame, text="Quantity:")
        quantityLabel.grid(row=3, column=0, sticky=W)
        quantityVar = StringVar()
        quantityVar.set(row[3])
        quantityEntry = Entry(frame, textvariable=quantityVar, state=DISABLED)
        quantityEntry.grid(row=3, column=1, sticky=W)

        # Price
        priceLabel = Label(frame, text="Price:")
        priceLabel.grid(row=4, column=0, sticky=W)
        priceVar = StringVar()
        priceVar.set(row[4])
        priceEntry = Entry(frame, textvariable=priceVar, state=DISABLED)
        priceEntry.grid(row=4, column=1, sticky=W)


    else:
        print("Select one item!!!")


def addEntry():

    addWindows = Toplevel()
    addWindows.title("Add Item")

    frame = Frame(addWindows)
    frame.pack()

    productLabel = Label(frame, text='Product:')
    productLabel.grid(row=0, column=0)
    productEntry = Entry(frame)
    productEntry.grid(row=0, column=1)

    descriptionLabel = Label(frame, text='Description:')
    descriptionLabel.grid(row=1, column=0)
    descriptionEntry = Entry(frame)
    descriptionEntry.grid(row=1, column=1)

    quantityLabel = Label(frame, text='Quantity:')
    quantityLabel.grid(row=2, column=0)
    quantityEntry = Entry(frame)
    quantityEntry.grid(row=2, column=1)

    priceLabel = Label(frame, text='Price:')
    priceLabel.grid(row=3, column=0)
    priceEntry = Entry(frame)
    priceEntry.grid(row=3, column=1)


    def saveItem():

        #Connection to DataBase
        db = pymysql.connect("localhost", "root", "everton", "guessBook")

        #Open cursor
        cursor = db.cursor()

        #sql query
        sql = sql = ("insert into tbproducts (product, description, quantity, price) values('%s', '%s', '%f', '%f')" %
       (str(productEntry.get()), str(descriptionEntry.get()), float(quantityEntry.get()), float(priceEntry.get())))

        try:
            cursor.execute(sql)
            db.commit()
            db.close()

        except Exception as e:
            print("Error to update DataBase " + e)
            db.rollback()
            db.close()
        else:
            print("Information was updated!")


        setList()



    saveButton = Button(frame, text='Save', command=saveItem)
    saveButton.grid(row=4, column=1, columnspan=2)


def updateEntry():
    pass

def deleteEntry():
    pass


def initWindow():

    windowInit = Tk()
    windowInit.title("Products")
    windowInit.geometry("300x300")

    global listProduct

    frame_01 = Frame(windowInit)
    frame_01.pack()

    loadButton = Button(frame_01, text=" Load ", command=loadEntry)
    addButton = Button(frame_01, text=" Add ", command=addEntry)
    updateButton = Button(frame_01, text="Update", command=updateEntry)
    deleteButton = Button(frame_01, text="Delete", command=deleteEntry)

    loadButton.pack(side=LEFT, pady=5)
    addButton.pack(side=LEFT, pady=5)
    updateButton.pack(side=LEFT, pady=5)
    deleteButton.pack(side=LEFT, pady=5)


    frame_02 = Frame(windowInit)
    frame_02.pack()

    scroll = Scrollbar(frame_02, orient=VERTICAL)
    listProduct = Listbox(frame_02, yscrollcommand=scroll, height=10)
    scroll.config(command=listProduct.yview)
    scroll.pack(side=RIGHT, fill=Y)
    listProduct.pack(side=LEFT, fill=BOTH, expand=1)
    return windowInit


def setList():

    listProduct.delete(0, END)
    #Open DataBase Connection
    db = pymysql.connect("localhost", "root", "everton", "guessBook")

    # prepare a cursor object using cursor() metho
    cursor = db.cursor()

    #SQL query
    sql = "select * from tbproducts"

    #Execute
    cursor.execute(sql)

    #Get one line
    row = cursor.fetchone()
    while row is not None:
        listProduct.insert(END, str(row[1]))
        row = cursor.fetchone()




win = initWindow()
setList()
win.mainloop()
