#! /usr/bin/Python
import cgi


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Form with CGI Python</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Complete Form Example</h2>")

print("<form method='POST' action='lesson_23_Form.py'>")
print("<p>First Name: <input type='text' name='txtName' /> </p>")
print("<p>Last Name: <input type='text' name='txtLastName' /> </p>")
print("<p><input type='radio' name='rblSex' value='Male'>Male <br>")
print("<input type='radio' name='rblSex' value='Female'>Female </p>")
print("<p>Company: <input type='text' name='txtCompany' /> </p>")
print(
    "<p>Favorite Color: <select name='selColor'> <option value='Select'>Select</option> <option value='Blue'>Blue</option> <option value='Red'>Red</option> </select> </p>")
print("<p><input type='Submit' value=Submit></p>")
print("</form>")

form = cgi.FieldStorage()

if len(form) > 0 and form["selColor"].value != "Select":

    print("<hr> <h3>Result: </h3>")

    if "txtName" in form:
        print("<p>Name : %s </p>" % form["txtName"].value)

    if "txtLastName" in form:
        print("<p>Last Name : %s </p>" % form["txtLastName"].value)

    if "rblSex" in form:
        print("<p>Sex : %s </p>" % form["rblSex"].value)

    if "txtCompany" in form:
        print("<p>Company : %s </p>" % form["txtCompany"].value)

    if "selColor" in form:
        print("<p>Favorite color : %s </p>" % form["selColor"].value)

printFooter()