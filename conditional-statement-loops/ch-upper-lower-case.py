# Check if the character given by the user is upercase or lowercase
character= input('Enter the character of your choice: ')
if character.isupper():
    print('Character is in uppercase')
elif character.islower():
    print('character is in lower case')
else:
    print('Not an alphabet!!!!')