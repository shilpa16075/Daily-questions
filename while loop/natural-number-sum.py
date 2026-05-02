# Write a program to print the sum of n natural numbers.
total_sum = 0
number = 1
n = 10
while number<=n:
    total_sum = total_sum+number
    print(total_sum)
    number+=1
    
print(f"The sum of first {n} is: {total_sum}")