# write a python program that take user's name as an input and prints: the first character 
# the last character and the length of the name.
name = input("Enter you good name: ")
print(name[0])   
# Negative indexing
print(name[-1])
print(name[-2])
# To access last characters of the unknown string we use str[-x:]
print(name[-3:])