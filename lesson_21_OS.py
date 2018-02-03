#! /usr/bin/Python
import os
import html

def printHeader():
    print("Content-type: text/html")
    print()
    print("<html>")
    print("<head><title>Information about system</title></head>")
    print("<body>")


def printFooter():
    print("</body>")
    print("</html>")


printHeader()

rowNumber = 0
backgroundColor = "white"

print("<table style='border:0'>")

for item in os.environ.keys():

    rowNumber += 1

    if rowNumber % 2 == 0:
        backgroundColor = "white"
    else:
        backgroundColor = "lightblue"

    print("<tr style='background-color: %s' <td>%s</td> <td>%s</td> </tr>" % (backgroundColor, html.escape(item),
                                                                              os.environ[item]))

print("</table>'")

printFooter()