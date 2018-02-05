#! /usr/bin/Python
import cgi


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Forms with CGI Python - Method Post</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Form with POST Method</h2>")

print(
    "<form method='POST' action='lesson_22_FormPost.py'> <p><input type='radio' name='rblSex' value='Male'>Male <br> <input type='radio' name='rblSex' value='Female'>Female <br> <input type='Submit' value='Submit' /> </p> </form")

pairs = cgi.parse()

if "rblSex" in pairs:
    print("<p> Your sex is: %s </p>" % pairs["rblSex"][0])

printFooter()