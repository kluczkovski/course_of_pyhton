#! /usr/bin/Python

import cgi


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Form with CGI - Files</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Form with CGI - Files</h2>")

print("<form method='POST' action='lesson_24_CGI_Files.py'>")
print("<p>Name: <input type='text' name='txtName'/> </p> ")
print("<p>Company: <input type='text' name='txtCompany'/> </p> ")
print(
    "<p>Color:  <select name='txtColor'> <option value='Select'>Select</option> <option value='Green'>Green </option> <option value=Blue>Blue</option> </select> </p>")
print("<p><input type='Submit' value='Submit' />")
print("</form>")

form = cgi.FieldStorage()

if len(form) > 0 and form["txtColor"].value != "Select":

    if "txtName" in form:
        print("<p> Name is %s </p>" % form["txtName"].value)

    if "txtCompany" in form:
        print("<p> Company is %s </p>" % form["txtCompany"].value)

    if "txtColor" in form:
        print("<p> Color is %s </p>" % form["txtColor"].value)

    with open('dataSave.txt', 'w') as fileOuput:
        fileOuput.write(form["txtName"].value + ";")
        fileOuput.write(form["txtCompany"].value + ";")
        fileOuput.write(form["txtColor"].value + ";")

    print("<hr> <h3>You saved the file </h3>")

printFooter()
