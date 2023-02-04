# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ne = 'Brad'
age_ne = 37

# Concatenate
print('Hello, my name is ' + name_ne + ' and I am ' + str(age_ne))

# String Formatting

# Arguments by position
print('My name is {name_ne} and I am {age_ne}'.format(name_ne = name_ne, age_ne = age_ne))

# F-Strings (3.6+)
print(f'Hello, my name is {name_ne} and I am {age_ne}')

# String Methods

s_ne = 'helloworld'

# Capitalize string
print(s_ne.capitalize())

# Make all uppercase
print(s_ne.upper())

# Make all lower
print(s_ne.lower())

# Swap case
print(s_ne.swapcase())

# Get length
print(len(s_ne))

# Replace
print(s_ne.replace('world', 'everyone'))

# Count
sub_ne = 'h'
print(s_ne.count(sub_ne))

# Starts with
print(s_ne.startswith('hello'))

# Ends with
print(s_ne.endswith('d'))

# Split into a list
print(s_ne.split())

# Find position
print(s_ne.find('r'))

# Is all alphanumeric
print(s_ne.isalnum())

# Is all alphabetic
print(s_ne.isalpha())

# Is all numeric
print(s.isnumeric())