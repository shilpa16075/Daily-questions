# Check if the string is palinedrome
word = input('Enter the word of your choice: ')
if word ==word[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome!!!")