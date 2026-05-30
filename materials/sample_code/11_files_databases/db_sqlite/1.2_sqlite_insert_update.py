import sqlite3

#  ################## INSERT DATA  ###########################################
db = sqlite3.connect('database.db')
# db.execute('drop table if exists person ')
# db.execute('create table person (firstname text, lastname text, age int)')
db.execute('INSERT INTO person (firstname, lastname, age) values ("Adam", "Anderson", 15)')
db.execute('INSERT INTO person (firstname, lastname, age) values ("Becky", "Brown", 37)')
db.execute('INSERT INTO person (firstname, lastname, age) values ("Charlotte", "Cooper", 37)')
db.execute('INSERT INTO person (firstname, lastname, age) values ("David", "Dixon", 55)')
db.commit()
# @@@@@@@@@@@@@@@@@@@@@@ DONE INSERTING DATA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#  ##################$# UPDATE DATA #########################################
# db = sqlite3.connect(database='database.db')
# db.execute('UPDATE person SET firstname = "TY" WHERE lastname = "Chen"')
# db.commit()

#  @@@@@@@@@@@@@@@@@@@@ DONE UPDATING DATA @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@