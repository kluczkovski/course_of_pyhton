import pymysql


db = pymysql.connect("localhost", "root", "everton", "guessBook")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchall()

print("Database version: %s" % data)

db.close()