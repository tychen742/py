import mysql_connector_OLD as conn

mydb = conn.mydb
cursor = mydb.cursor()

cursor.execute(
    "USE mydatabase")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

cursor.execute(sql, val)
mydb.commit()

print(cursor.rowcount, "record inserted.")


cursor.close()          # ### close recommended
mydb.close()            # ### close recommended
