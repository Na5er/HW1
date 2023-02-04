# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_ne = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile_ne.name)
print('Is Closed : ', myFile_ne.closed)
print('Opening Mode: ', myFile_ne.mode)

# Write to file
myFile_ne.write('I love Python')
myFile_ne.write(' and JavaScript')
myFile_ne.close()

# Append to file
myFile_ne = open('myfile.txt', 'a')
myFile_ne.write(' I also like PHP')
myFile_ne.close()

# Read from file
myFile_ne = open('myfile.txt', 'r+')
text_ne = myFile_ne.read(100)
print(text_ne)
