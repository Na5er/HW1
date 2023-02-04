# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

 x_ne = 7            # int
 y_ne = 5.5          # float
 name = 'Nasser'  # str
 is_cool = True   # bool
 
x_ne , y_ne, name, is_cool = (7, 5.5, 'John', True)

a_ne = x_ne + y_ne

x_ne = str(x_ne)
y_ne = int(y_ne)
z_ne = float(y_ne)

print(type(z_ne), z_ne)
