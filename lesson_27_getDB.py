#! /usr/local/bin/Python3

import cgi
import pymysql
import cgitb

cgitb.enable()


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>List information from guesses table</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


def getInformation():
    # Open DataBase
    db = pymysql.connect("localhost", "root", "everton", "guessBook")

    cursor = db.cursor()

    cursor.execute("select * from guesses")

    row = cursor.fetchone()

    print("<table border=1>")
    while row is not None:
        print("<tr>")
        print("<td>" + str(row[0]) + "</td>")
        print("<td>" + str(row[1]) + "</td>")
        print("<td>" + str(row[2]) + "</td>")
        print("<td>" + str(row[3]) + "</td>")
        print("<td>" + str(row[4]) + "</td>")
        print("<td>" + str(row[5]) + "</td>")
        print("</tr>")

        row = cursor.fetchone()

    print("</table>")
    cursor.close()
    db.close()


printHeader()

print("<h3>List information from guesses table:</h3>")
print("<tr>")

getInformation()

print("<tr>")

printFooter()