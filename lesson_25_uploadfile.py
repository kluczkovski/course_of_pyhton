#! /usr/bin/Python

import cgi
import os
import sys


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Upload a file - CGI Python</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

form = cgi.FieldStorage();
fileitem = form["filename"]

if "filename" in form:

    # fn = os.path.basename(fileitem.filename)
    # open("./upload/" + fn, 'wb').write(fileitem.file.read())
    file_name = fileitem.filename
    mypath = ("./upload/" + file_name)
    with open(mypath, 'wb') as tmpFile:
        tmpFile.write(fileitem.file.read())


else:

    print("Field is not found")

printFooter()