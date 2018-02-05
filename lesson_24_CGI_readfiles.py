#! /usr/bin/Python

import cgi


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Form with CGI - Read File</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Form with CGI - Read Files")
print("<br>")

print("<form method='POST' action='lesson_24_CGI_readfiles.py' enctype='multipart/form-data'")
print("<p>File: <input type='file' name='file'> </p>")
print("<input type='Submit' name='submit'>")
print("</form>")

form = cgi.FieldStorage()

if "file" in form:

    fileitem = form["file"]

    if not fileitem.file:
        print("<h3>No File found </h3>")
    else:
        text_file = open(fileitem.filename, "r")
        print("Result:")

        for lines in text_file:
            datas = lines.split(";")
            print("<p>Name: %s </p>" % datas[0])
            print("<p>Company: %s </p>" % datas[1])
            print("<p>Color: %s </p>" % datas[2])


else:
    print("No file select")

printFooter()