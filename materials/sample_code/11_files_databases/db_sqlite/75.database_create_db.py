import sqlite3
# import math

db = sqlite3.connect('database.db')

db.execute('DROP TABLE IF EXISTS person')
# db.execute('drop table if exists people')

db.execute('create table person(firstname text, lastname text, age int)')
# db.execute('create table people(firstname text, lastname text, age int)')


