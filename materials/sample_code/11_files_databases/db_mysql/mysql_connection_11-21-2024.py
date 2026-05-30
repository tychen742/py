import mysql.connector
# import pymysql

passwd = 'passwd@2020'
conn = mysql.connector.connect(
  host="localhost",
  user="salesadmin",
  password='pass2020@@',
  db='sales',
)

print(conn)