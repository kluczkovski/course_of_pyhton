#! /usr/local/bin/Python3

import pymysql
import cgi
import cgitb
import datetime

cgitb.enable()


def printHeader():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<head><title>Guess Book - CGI Write to MYSQL</title></head>")
    print("<body>")


def printFooter():
    print("</body></html>")


def updateDB():
    # Open database connection
    db = pymysql.connect("localhost", "root", "everton", "guessBook")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = ("insert into guesses (name, lastname, email, date, message) values('%s', '%s', '%s', '%s', '%s')" % (
    name, lastName, email, myDateTime, message))

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("Exception : %s" % e)
        db.rollback()
        cursor.close()
        db.close()
    else:
        print("Information were recorded with sucessful!!!")
        cursor.close()
        db.close()


printHeader()
form = cgi.FieldStorage()

if len(form) > 0:
    name = form["txtName"].value
    lastName = form["txtLastName"].value
    email = form["txtEmail"].value
    myDateTime = datetime.datetime.now();
    message = form["txtMessage"].value

    updateDB()

    print("<hr>")
    print("<h3>Result:</h3>")
    print("my name is : %s" % name)
    print("my last name is : %s" % lastName)
    print("my email is : %s" % email)
    print("my message is : %s" % message)

printFooter()
