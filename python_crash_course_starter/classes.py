# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class user_ne:

  # Constructor
  def __init__(self, name_ne, email_ne, age_ne):
    self.name_ne = name_ne
    self.email_ne = email_ne
    self.age_ne = age_ne
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):
      return f'My name_ne is {self.name_ne} and I am {self.age_ne}'

  def has_birthday(self):
      self.age_ne += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(user_ne):
  # Constructor
  def __init__(self, name_ne, email_ne, age_ne):
      user_ne.__init__(self, name_ne, email_ne, age_ne) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name_ne = name_ne
      self.email_ne = email_ne
      self.age_ne = age_ne
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name_ne is {self.name_ne} and I am {self.age_ne} and my balance is {self.balance}'

#  Init user_neuser_ne object
brad_ne = user_ne('Brad Traversy', 'brad_ne@gmail.com', 37)
# Init customer object
Janet_ne = Customer('Janet_neJanet_ne Johnson', 'Janet_ne@yahoo.com', 25)

Janet_ne.set_balance(500)
print(Janet_ne.greeting())

brad_ne.has_birthday()
print(brad_ne.greeting())

#Encapsulation -->
brad_ne.print_encap()
brad_ne._private = 800 #Changing for brad_ne
brad_ne.print_encap()

# Method inherited from parent
Janet_ne.print_encap() #Changing the variable for brad_ne doesn't affect Janet_nes variable --> Encapsulation
Janet_ne._private = 600
Janet_ne.print_encap()

#Similary changing Janet_ne's doesn't affect brad_ne's variable.
brad_ne.print_encap()