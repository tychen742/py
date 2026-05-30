from mysqltest.conn import connect_to
dbconn = connect_to('test')
cursor = dbconn.cursor()


##### UPDATE Statement:  modify the existing records in a table
##### syntax: UPDATE SET WHERE (WHERE is "optional" but CRITICAL)

##### ALTER TABLE statement: modify columns in existing table 

### ADD, DROP
# sql = "ALTER TABLE user ADD fname varchar(64)"
# sql = "ALTER TABLE user DROP COLUMN fname"
# sql = "ALTER TABLE user ADD first_name varchar(255)"
# sql = "ALTER TABLE user ADD email varchar(255)"
# sql = "ALTER TABLE user ADD PRIMARY KEY (id)"
# sql = "ALTER TABLE user MODIFY id INT AUTO_INCREMENT NOT NULL PRIMARY KEY"
sql = "ALTER TABLE user MODIFY id INT AUTO_INCREMENT NOT NULL"
# sql = "UPDATE users SET address = 'Canyon 123' WHERE address = 'Valley 345'"

cursor.execute(sql)

dbconn.commit()
cursor.close()
dbconn.close()