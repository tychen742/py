from mysql_conn import connect_to

dbconn = connect_to('hbdi')
cursor = dbconn.cursor()


SQL = 'INSERT INTO user (name_first, name_last, email) VALUES (%s, %s, %s)'
# values = ('TY', 'Chen', 'tychen742@gmail.com')
# values = ('Keanu', 'Reeves', 'reeves@gmail.com')
# values = ('John', 'Doe', 'jd@gmail.com')
values = ('Jane', 'Doe', 'janed@gmail.com')

cursor.execute(SQL, values)
result = cursor.fetchall()

for x in result:
    print(x)

dbconn.commit()
cursor.close()
dbconn.close()