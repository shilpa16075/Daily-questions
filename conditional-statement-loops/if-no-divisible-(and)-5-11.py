# Check the user input is divisible by 5 and 11
a = int(input("Enter your number: "))
if (a%5==0)and(a%11==0):
    print('Number is divisible by 5 and 11')
else:
    print('Number is not divisible by 5 and 11')