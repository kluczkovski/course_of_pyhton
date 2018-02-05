#! /usr/bin/Python

import cgi


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Forms with CGI Python - GET</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


printHeader()

print("<h2>Form with GET Method</h2>")

print("<form method='GET' action='lesson_22_Form.py'> <p> Company: <input type='text' name='txtCompany' /> <br> <input type='submit' value='submit' /> </p> </form")


pairs = cgi.parse()


if "txtCompany" in pairs:
    #print("<p> Your company is: %s" % (cgi.parse(pairs["txtCompany"][0])))
    print("<p> Your company is: %s </p>" % (pairs["txtCompany"][0]) )

printFooter()
