import mysql.connector as conn


try:    # ### just like files, connections are prone to errors
        # ### mydb (cnx) is just a variable 
    db = conn.connect(
        host="localhost",
        user="chen_user",
        password="passwd2024"
    )
    # print(db)
    cursor = db.cursor()
except Exception as e:
    print(f"An error occured when establishing connection: {e}")
    exit()


if __name__ == "__main__":
    # Conn1= Conn()
    print(f"Print mydb: {db}")
    print("Say something")
 