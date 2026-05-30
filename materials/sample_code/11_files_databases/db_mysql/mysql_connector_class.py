import mysql.connector as mysql

# ### https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class
class ConnClass:
    def __init__(self, database):
        self.database = database

    # def conn(self):
        # try:    # ### just like files, connections are prone to errors
            # ### mydb (cnx) is just a variable
        self._conn = mysql.connect(
            host="localhost",
            user="chen_user",
            password="passwd2024",
            database=self.database
        )
        self._cursor = self._conn.cursor()
    
    # ### https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
    # ### enter and exit enable with
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
    # ### @property decorator: getter/setter
    @property
    def connection(self):
        return self._conn           # ### _ decorator: private variable
    
    @property
    def cursor(self):
        return self._cursor
    
    
    def commit(self):
        self.connection.commit()
        
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
            
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        
    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
 
        
# print(mydb)
# cursor = mydb.cursor()
# except Exception as e:
#     print(f"An error occured when establishing connection: {e}")
#     exit()

# if __name__ == "__main__":
#     # Conn1= Conn()
#     print(f"Print mydb: {mydb}")
#     print("Say something")