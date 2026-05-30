from mysql_connector_class import ConnClass
import csv

with ConnClass("employees") as db:
  sql = "SELECT D.dept_no, D.dept_name, \
  E.emp_no, E.first_name, E.last_name \
  FROM employees AS E \
  INNER JOIN dept_manager AS DM ON E.emp_no = DM.emp_no \
      INNER JOIN departments AS D ON DM.dept_no = D.dept_no \
          WHERE DM.to_date = '9999-01-01'"
  db.cursor.execute(sql)
  result = db.cursor.fetchall()

fields = ['dept_no', 'dept_name', 'emp_no', 'first_name', 'last_name']
filename = 'employeee.csv'
with open (filename, 'w', newline='') as outcsv:
  writer=csv.writer(outcsv)
  writer.writerow(fields)

with open (filename, 'a', newline = '') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')
  writer.writerows(result)  

db.cursor.close()
# conn.close()


# ### https://stackoverflow.com/questions/4613465/using-python-to-write-mysql-query-to-csv-need-to-show-field-names
# fp = open(filename, mode = 'a', newline='')
# myFile = csv.writer(fp, delimiter=',')
# # myFile.writerow(fields)
# myFile.writerows(result)
# fp.close()