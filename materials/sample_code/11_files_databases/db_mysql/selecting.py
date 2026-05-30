import mysql_conn as conn
cnx = conn.connect_to('hbdi')
cursor = cnx.cursor()

sql = "SELECT name_last, name_first FROM user LIMIT 10"
cursor.execute(sql)
result = cursor.fetchall()      # ### fetch all rows
for x in result:
    print(x)
# cnx.commit            # ### needed if changing the DB
cursor.close()          # ### close recommended
cnx.close()             # ### close recommended

