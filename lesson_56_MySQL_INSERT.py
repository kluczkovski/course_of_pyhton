
import pymysql
import datetime



# Open dataBase Connection
db = pymysql.connect("localhost", "root", "everton", "guessBook")

# prepare a cursor object using cursor() metho
cursor = db.cursor()

# prepare SQL query to insert a record into the database
product='product 04'
description = "description product 04"
quantity = 4000.0
price = 10.45
sql = ("insert into tbproducts (product, description, quantity, price) values('%s', '%s', '%f', '%f')" %
       (product, description, quantity, price))

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print("Exception: %s" %e)
    db.rollback()
    db.close()
else:
    print("Information were updated without problem")
    db.close()
