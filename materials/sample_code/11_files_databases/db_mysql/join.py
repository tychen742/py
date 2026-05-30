import mysql_conn as conn

dbconn = conn.connect_to('hbdi')
cursor = dbconn.cursor()

print("SHOW TABLES")






cursor.close()
dbconn.close()