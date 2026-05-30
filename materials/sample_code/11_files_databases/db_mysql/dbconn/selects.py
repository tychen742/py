import mysqltest.conn as db 

dbconn = db.connect_to('hbdi')
cursor = dbconn.cursor()


# SQL = 'SELECT * FROM user'
SQL = 'SHOW TABLES;'
cursor.execute(SQL)
result = cursor.fetchall()

# print("HUH")

for x in result:
    print(x)
    # print("WHAT")


cursor.close()
dbconn.close()
