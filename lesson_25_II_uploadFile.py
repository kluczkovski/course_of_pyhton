#! /usr/bin/Python

import cgi
import cgitb
import os

cgitb.enable()


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Upload File - Lesson 25 II</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


myPath = "./upload/"

printHeader()

form = cgi.FieldStorage();

if "filename" in form:
    file_name = form["filename"]

    with open(myPath + file_name.filename, "w+") as myFile:
        myFile.write(file_name.file.read())

        print("<p> Your file %s was saved </p" % file_name.filename)

        print("<p> Link for to file <a href='./upload/%s' target='_blank'> Your file </a>" % file_name.filename)

printFooter()