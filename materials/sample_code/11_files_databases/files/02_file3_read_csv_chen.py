# ##### read CSV files #####

# ### import 
import csv

import os.path
data_path = '/Users/tcn85/workspace/class/jupyter/data/'

with open(os.path.join(data_path, 'members_chen.csv'), newline='') as csvfile:
    persons = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in persons:
        print(', '.join(row))
        
        
        