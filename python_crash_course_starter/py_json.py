# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_ne = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_ne = json.loads(userJSON)

# print(user_ne)
# print(user_ne['first_name'])

car_ne = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_ne= json.dumps(car_ne)

print(carJSON_ne)