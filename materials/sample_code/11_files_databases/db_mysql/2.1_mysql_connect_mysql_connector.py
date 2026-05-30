import mysql.connector
# import pandas as pd
import logging
import sshtunnel
# from sshtunnel import SSHTunnelForwarder


ssh_host = "74.208.29.196"
ssh_port = 22
ssh_username = "chen_user"
ssh_password = "passwd@2020"

localhost = '127.0.0.1'

database_name = "employees"
database_username = 'chen_user'
database_password = 'passwd2024'


with sshtunnel.SSHTunnelForwarder(
    (ssh_host, 22),
    ssh_username=ssh_username,
    ssh_password=ssh_password,
    remote_bind_address=('127.0.0.1', 3306)

) as tunnel:
    print("test")
    tunnel.start()
    dbconn = mysql.connector.connect(
        host='127.0.0.1',
        user='chen_user',
        password='passwd2024',
        database=database_name,
        # port = 3306,
        use_pure = True,
        port=tunnel.local_bind_port
    )

    cursor = dbconn.cursor()

    cursor.execute("SELECT * FROM departments")
    for row in cursor:
        print(row)
# print(mycursor("SHOW TABLES"))


# ##### run_querry()
# df = run_query("SELECT id, task, date FROM todo WHERE project = 'todo' " )
# print(df.head())

# ##### cursor
# cursor = connection.cursor()
# print(cursor.execute("SHOW TABLES"))

# mysql_disconnect()
# close_ssh_tunnel()
