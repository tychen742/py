### this has no ssh so it will not work

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='chen_user', passwd='redcar2024', database='employees')
cursor = cnx.cursor()

# query = ("SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN %s AND %s")
query = ("SELECT first_name, last_name, hire_date FROM employees WHERE to_date = '9999-01-01' ")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

# cursor.execute(query, (hire_start, hire_end))
cursor.execute(query)

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()