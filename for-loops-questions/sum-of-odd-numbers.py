# program to print the sum of all the odd numbers within a given range.
a = int(input('enter the starting value: '))
b = int(input('enter the end value: '))
sum = 0
for i in range(a,b,2):
    sum=sum+i
    print(sum)
