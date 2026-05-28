# write a program to print average of 10 numbers
digit_sum = 0
i = 0 
while i<10:
    num = int(input('enter the number: '))
    digit_sum =digit_sum+num
    i+=1
print(digit_sum/2)