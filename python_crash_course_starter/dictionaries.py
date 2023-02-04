# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person_ne = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_ne = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_ne['first_name'])
print(person_ne.get('last_name'))

# Add key/value
person_ne['phone'] = '555-555-5555'

# Get dict keys
print(person_ne.keys())

# Get dict items
print(person_ne.items())

# Copy dict
person2_ne = person_ne.copy()
person2_ne['city'] = 'Boston'

# Remove item
del(person_ne['age'])
person_ne.pop('phone')

# Clear
person_ne.clear()

# Get length
print(len(person2_ne))

# List of dict
people_ne = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people_ne[1]['name'])