# If/ Else conditions are used to decide to do something based on something being true or false

x_ne = 21
y_ne = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ne > y_ne:
  print(f'{x_ne} is greater than {y_ne}')

# If/else
if x_ne > y_ne:
  print(f'{x_ne} is greater than {y_ne}')
else:
  print(f'{y_ne} is greater than {x_ne}')  

# elif
if x_ne > y_ne:
  print(f'{x_ne} is greater than {y_ne}')
elif x_ne == y_ne:
  print(f'{x_ne} is equal to {y_ne}')  
else:
  print(f'{y_ne} is greater than {x_ne}')  

# Nested if
if x_ne > 2:
  if x_ne <= 10:
    print(f'{x_ne} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_ne > 2 and x_ne <= 10:
    print(f'{x_ne} is greater than 2 and less than or equal to 10')

# or
if x_ne > 2 or x_ne <= 10:
    print(f'{x_ne} is greater than 2 or less than or equal to 10')

# not
if not(x_ne == y_ne):
  print(f'{x_ne} is not equal to {y_ne}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers_ne = [1,2,3,4,5]

#  in
if x_ne in numbers_ne:
  print(x_ne in numbers_ne)

# not in
if x_ne not in numbers_ne:
  print(x_ne not in numbers_ne)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_ne is y_ne:
  print(x_ne is y_ne)

# is not
if x_ne is not y_ne:
  print(x_ne is not y_ne)

