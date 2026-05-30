
# ### JSON == JavaScript object notation 

import json

# a JSON object:
json_dict =  '{ "name":"TY Chen", "age":35, "city":"Charlottsville"}'

# parse json_dict:
dict = json.loads(json_dict)

# the result is a Python dictionary:
print(dict["age"])