

# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_ne = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_ne = ('Apples',)

# Get value
print(fruits_ne[1])

# Can't change value
fruits_ne[0] = 'Pears'

# Delete tuple
del fruits2_ne

# Get length
print(len(fruits_ne))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_ne_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_ne_set)

# Add to set
fruits_ne_set.add('Grape')

# Remove from set
fruits_ne_set.remove('Grape')

# Add duplicate
fruits_ne_set.add('Apples')

# Clear set
fruits_ne_set.clear()

# Delete
del fruits_ne_set

print(fruits_ne_set)
