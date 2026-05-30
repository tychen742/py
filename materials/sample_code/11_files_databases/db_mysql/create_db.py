import mysql_connector_OLD as conn    # ### this will run the connector file
                                  # ### and make the mydb variable available

# conn = new Conn()
mydb = conn.mydb                  # ### we want that variable
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="chen_user",
#   password="passwd2024"
# )

cursor = conn.cursor

try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;") # ### note the IF NOT EXISTS
    mydb.commit()       # ### commit() recommended
    print("working...")
except Exception as e:
    print(f"An error occured when establishing connection: {e}")
    exit()


cursor.close()          # ### close recommended
mydb.close()            # ### close recommended
