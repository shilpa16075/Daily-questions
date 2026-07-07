# write a python program that accept the user word than reverse it.
word = input('enter the word of your choice: ')
reversed = ''
for i in word:
    reversed = i+reversed
print(reversed)