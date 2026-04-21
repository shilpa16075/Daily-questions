# python program to check if the given word from the user is a palindrome.
word = input("enter the word for palindrome check: ")
reversed_string = ""
for element in word:
    reversed_string = element+reversed_string
print(reversed_string)
if word==reversed_string:
    print("this is a palindrome",reversed_string)
else:
    print('this is not a palindrome',word)