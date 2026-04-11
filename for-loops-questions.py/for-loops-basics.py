#  program to demonstrate the use of for loop 
n = int(input("enter the number of your choice: "))    #suppose n = 7
sum = 0                                                #sum of first natural number is 1 
for i in range(1,1+n):                                 #range(1,8) because end element is not included but we need sum upto the value n  
    sum+=i
    print("sum of n",n,"natural numbers is :",sum)