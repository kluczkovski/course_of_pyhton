#! /usr/bin/Python
import os
import cgi
import urllib.parse


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Get information by Query String</title></head>")
    print("<body>")


def printFooter():
    print("</body>")
    print("</html>")


printHeader()

print("<h2>Query String</h2>")

query = os.environ["QUERY_STRING"]

if len(query) == 0:
    print("<p> No information was passed")
else:
    print("<p style='font-style:italic'>The query string is " + cgi.escape(query))
    pairs = cgi.parse_qs(query)
    pairs = urllib.parse.parse_qs(query)

    for key, value in pairs.items():
        print("<p> you set query string %s to value %s </p>" % (key, value))

printFooter()
