# Write a program to print multiplication table of any number entered by the user for the loop.
n = int(input("enter a number : ")) 
for i in range(1,11):
    print(n,"x",i,"=",n*i)
# let's assume n = 3
# n = 3 i = 1 , 3 x 1 = 3*1
# n = 3 i = 2 , 3 x 2 = 3*2
# n = 3 i = 3 , 3 x 3 = 3*3
# n = 4
# n = 3 i = 10 , 3 x 10 = 3*10 