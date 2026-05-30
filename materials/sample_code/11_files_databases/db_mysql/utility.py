import mysql.connector

cnx = mysql.connector.connect(user='chen_user', passwd='passwd2024', database='employees')
cursor = cnx.cursor(buffered=True)


# query = ("SELECT first_name, last_name, hire_date FROM employees WHERE to_date = '9999-01-01' ")
query = ("SELECT * FROM employees LIMIT 3")


cursor.execute(query)

for (first_name) in cursor:
    # print(last_name, first_name)
    print("{} ".format(first_name))


cursor.close()
cnx.close()