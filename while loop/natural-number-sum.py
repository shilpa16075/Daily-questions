# Write a program to print the sum of n natural numbers.
sum = 0
number = 1
n = 10
while number<=n:
    sum = sum+number
    print(sum)
    number+=1
    
print(f"The sum of first {n} is: {sum}")