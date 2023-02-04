# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ne = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people_ne:
  print(f'Current Person: {person}')

# Break
for person in people_ne:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for person in people_ne:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range
for i in range(len(people_ne)):
  print(people_ne[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_ne = 0
while count_ne < 10:
  print(f'Count: {count_ne}')
  count_ne += 1