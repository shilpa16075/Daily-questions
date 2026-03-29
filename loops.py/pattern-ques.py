#  write a program to print pattern using for and while loop 
# *
# **
# ***
# ****
# *****     
for  i in range (1,7):
    print("*"*i)
#  reverse the same pattern 
for i in range(6,0,-1):
    print("*"*i)


n = 1
while n<=6:
    print("*"*n)   # print string * the value of n 
    n=n+1          # increment to next value



# reverse pattern 
n = 6             # initial value     
while n>=0:       # condition
    print("*"* n) 
    n = n-1       # decrement 

