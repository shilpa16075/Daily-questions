#  Sometimes, depending on the situation, we want to terminate the loop in the middle of the iteration. The break statement allows us to break the loop at any point of the iteration.
#  find the sum of the first n number, but if the sum is greater than 100, then stop the iteration
# sum1 = 0 
# num = int(input("enter the number: "))
# for each in range(1,num):
#     sum1 = sum+each 
#     if sum1>100: 
#         break
# print("total number is ", sum1)
#  break statement within while loop 
sum1 = 0 
while True:
    n = int(input("enter the number to add : or press 0 to exit "))
    sum1 = sum1 + n 
    print("sum1: ", sum1 )
    if n ==0:
        break
print("total is ", sum1)      
#  Continue statement : It is used to skip tje current iteration.
#  With the continue statement, the loop does not terminate, but continue with the next iteration. 
list1 = [1,2,3,4,5,6,7,8,9]
for i in list1: 
    c = 10/i*100
    print("percent is ", c)