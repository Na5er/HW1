# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today_ne = date.today_ne()
timestamp_ne = time_ne()

c_ne = CamelCase()
# print(c_ne.hump('hello there world'))

email_ne = 'test#test.com'
if validate_email(email_ne):
  print('Email is valid')
else:
  print('Email is bad')