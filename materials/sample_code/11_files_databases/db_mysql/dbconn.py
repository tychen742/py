# import mysql.connector
from mysql.connector import connect
import pandas as pd
import logging
import pymysql
import pymysql.cursors
import sshtunnel
from sshtunnel import SSHTunnelForwarder

ssh_host = "tychen.org"
ssh_username = "tychen"
ssh_password = "Redcar@@2020"

localhost = '127.0.0.1'
database_username = 'tychen'
database_password = 'Redcar@@2020'
database_name = "test"


def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """

    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=('127.0.0.1', 3306)
    )

    tunnel.start()


def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection

    :return connection: Global MySQL database connection
    """

    global connection

    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port,
        cursorclass=pymysql.cursors.DictCursor
    )

def run_query(sql):
  """Runs a given SQL query via the global database connection.

  :param sql: MySQL query
  :return: Pandas dataframe containing results
  """
  return pd.read_sql_query(sql, connection)

def mysql_disconnect():
    """Closes the MySQL database connection.
    """
    connection.close()

def close_ssh_tunnel():
    """Closes the SSH tunnel connection.
    """    
    tunnel.close




open_ssh_tunnel()
mysql_connect()

# # ### get a list of dictionary because of cursor 
# with connection.cursor() as cursor:
#     sql = "SELECT id, task, date FROM todo"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     # print(result)
#     for i in result:
#         print(i)




# ##### run_querry()
# df = run_query("SELECT id, task, date FROM todo WHERE project = 'todo' " )
# print(df.head())    ### got the keys


# print(run_query("USE test"))
# print(run_query("SHOW TABLES"))

# ##### cursor
# cursor = connection.cursor()
# print(cursor.execute("SHOW TABLES"))

# mysql_disconnect()
# close_ssh_tunnel()