#  Sometimes, depending on the situation, we want to terminate the loop in the middle of the iteration. The break statement allows us to break the loop at any point of the iteration.
#  find the sum of the first n number, but if the sum is greater than 100, then stop the iteration
sum = 0 
num = int(input("enter the number: "))
for each in range(1,num):
    sum = sum+each 
    if sum>100: 
        break
print("total number is ", sum)