# import mysql_connection
from mysqltest.conn import connect_to


# The process: https://stackoverflow.com/questions/5504340/python-mysqldb-connection-close-vs-cursor-close
# 1 Create connection
# 2 Create cursor
# 3 Create Query string
# 4 Execute the query
# 5 Commit to the query
# 6 Close the cursor
# 7 Close the connection


# dbconn = mysql_connection.connect_to('test')
dbconn = connect_to('test')
cursor = dbconn.cursor()


# check if DB exists
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)


# show tables
cursor.execute("SHOW TABLES;")
for x in cursor:
    print(x)

cursor.execute("DESCRIBE user")
for x in cursor:
    print(x)

cursor.close()
dbconn.close()
