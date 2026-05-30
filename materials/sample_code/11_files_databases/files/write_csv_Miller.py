# ### write a CSV file
import csv

# ### csv.writer()
# csv.writer(csvfile="", dialect="excel")
# csv.writer(csvfile="")

# ##### csv.writer()
# ##### the with statement has exception handling
# ### writer() has a writerow() method
# ### do: open(), writerow()
with open('members_Miller.csv', 'w', newline='') as file:
    writer = csv.writer(file)   # CSV writer object writing to file
    field = ["name", "age", "country"]  # list

    writer.writerow(field)
    writer.writerow(["Keanu Reeves", "55", "USA"])  # list
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "Taiwan"])

    