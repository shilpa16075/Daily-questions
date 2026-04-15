# Check if the string is palindrome
word = input('Enter the word of your choice: ')
clean_word = word.replace(" ","").lower()  # remove space(nurses run) and convert into lower or uppercase 
if clean_word ==clean_word[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome!!!")