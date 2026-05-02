# program to print the sum of all numbers from 1 to given number.
x = int(input('Enter the range value: '))
total_sum = 0
for i in range(1,x):
    total_sum = total_sum +i
    print(total_sum)