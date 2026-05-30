import mysql_connector_OLD as conn

mydb = conn.mydb

cursor = mydb.cursor()
cursor.execute(
    "USE mydatabase")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

cursor.execute("SHOW TABLES")       # ### note this is a second cursor ==> one connection >1 cursor

# cursor.execute(
#     "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


for x in cursor:
    print(x)

mydb.commit()           # ### in case auto-commit is not enabled
##### add id column #####


cursor.close()          # ### close recommended
mydb.close()            # ### close recommended