import sqlite3

db = sqlite3.connect('database.db')
table = db.execute('SELECT * FROM person')
for each in table:
    print(each)
    # print(each['firstname'])
    print(each[0])


# db = sqlite3.connect('database.db')
# db.row_factory = sqlite3.Row
# table = db.execute('SELECT * FROM person')
# for each in table:
#     print(dict(each))


#  ################# DELETE ###################
# db.execute('DELETE FROM person WHERE lastname = "Clint"')
# db.commit()

# print("Deleted.")

db = sqlite3.connect('database.db') #  If you don't do this, you get object, not data.
table = db.execute("SELECT * FROM person")
for each in table:
    print(each)
