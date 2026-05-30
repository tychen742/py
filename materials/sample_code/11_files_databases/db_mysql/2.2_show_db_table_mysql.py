import dbconn
import pandas as pd


dbconn.open_ssh_tunnel()
dbconn.mysql_connect()


# ##### SHOW DATABASES  #####

# ### gives key Database
# sql = "SHOW DATABASES"
# result = dbconn.run_query(sql)   
# print(result)

# ### showing keys (Database)
# sql = "SHOW DATABASES"
# result = pd.DataFrame(dbconn.run_query(sql))
# print(result)  

# ### gives the number of DBs
# sql = "SHOW DATABASES"
# with dbconn.connection.cursor() as cursor:  
#     result = cursor.execute(sql)
#     print(result)

# ### offsets error
# sql = "SHOW DATABASES"
# with dbconn.connection.cursor() as cursor:  
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     df = pd.DateOffset(result)
#     print(df)


# ##### SHOW TABLES
sql = "SHOW TABLES"
with dbconn.connection.cursor() as cursor :
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    print(df)
 


# ##### SELECT using cursor for tychen DB###
# requires df DataFrame or will only show dictionary keys
"""
sql = "SELECT id, task, date FROM todo"
with dbconn.connection.cursor() as cursor:
    cursor.execute(sql)
    # result = cursor.fetchall()
    # for i in result:      ### output a list (dictionary each line)
    #     print(i)
    
    result = cursor.fetchall()
    df = pd.DataFrame(result)   ### works
    print(df)
"""

# ##### SELECT using run_query    
"""
sql = "SELECT id, task, date FROM tychen.todo"
result = dbconn.run_query(sql)
print(result)
"""






"""     @@@@ does not work @@@
sql = 'SELECT DB_NAME()'
with dbconn.connection.cursor() as cursor:
    cursor.execute(sql)
"""
