# Check if the string is palindrome
word = input('Enter the word of your choice: ')
clean_word = word.replace(" ","").lower()
if clean_word ==clean_word[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome!!!")