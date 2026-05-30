# pip install mysql.connector installed but says
# "ModuleNotFoundError: No module named 'mysql.connector'; 'mysql' is not a package"

# XXX pip install mysql-connector-python-rf
# XXX https://stackoverflow.com/questions/32877671/importerror-no-module-named-mysql

# just use this; maintained and updated


# pip install mysql-connector-python    ### mysql-connector in dev.mysql.com does not work for me
# pip install sshtunnel

import mysql.connector as db
# import mysql.connector
# from mysql.connector import connect
import sshtunnel

SSH_HOST = '108.175.15.210'
SSH_PORT = 22
SSH_USERNAME = 'tychen'
# SSH_PKEY = '/Users/tychen/.ssh/id_ed25519'
SSH_PASSWORD = 'Redcar@@2020'

DB_HOST = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = 'Redcar@@2020'
remote_bind_address = ('localhost', 3306)


##########
# this works: https://stackoverflow.com/questions/21903411/enable-python-to-connect-to-mysql-via-ssh-tunnelling/51116269
##########
# the difference is tunnel.start()
tunnel = sshtunnel.SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),             
    ssh_username=SSH_USERNAME,                                      
    ssh_password=SSH_PASSWORD,
    remote_bind_address=(DB_HOST, 3306))
tunnel.start()
# with sshtunnel.SSHTunnelForwarder(
#     ('tychen.org', 22),
#     ssh_username='tychen',
#     ssh_password='Redcar@@2020',
#     ssh_pkey='/Users/tychen/.ssh/id_ed25519',
#     remote_bind_address=('localhost', 3306),
# ) as tunnel:
#     tunnel.start()


# MySQLConnection, not connect, from https://stackoverflow.com/questions/21903411/enable-python-to-connect-to-mysql-via-ssh-tunnelling/51116269
def connect_to(db_name):
    # dbconn = db.connect(  ### this is the old way and not working
    dbconn = db.MySQLConnection(
        host=DB_HOST, user=DB_USERNAME, password=DB_PASSWORD,
        db=db_name, port=tunnel.local_bind_port
    )
    return dbconn


# print(dbconn)
