import dbconn
import pandas as pd

"""
# ##### the test db is empty
sql = "SHOW TABLES"
with dbconn.connection.cursor() as cursor :
    cursor.execute(sql)
    result = cursor.fetchall()
    # for i in result:
    #     print(i)

    df = pd.DataFrame(result)
    print(df)
"""


# ##### create a table in test DB: works
# must have at least 1 column when creating
"""
sql = "CREATE TABLE IF NOT EXISTS user (id int(5) NOT NULL, last_name VARCHAR(255))"
with dbconn.connection.cursor() as cursor:
    cursor.execute(sql)
"""

# ##### create a new db: works
"""
sql = "CREATE DATABASE IF NOT EXISTS test2"
with dbconn.connection.cursor() as cursor:
    cursor.execute(sql)
"""

