# Check if the number is prime number or not.
num = int(input('enter the number of your choice: '))       #let's suppose num = 7
count= 0
for i in range(1,num+1):         # range(1,2,3,4,5,6,7)
    if num%i==0:                 # this will check if any number from the range is dividing the num or not.
        count+=1                 # increment if factor is found
if count == 2:                   # if factor are equal to 2 then num is prime 
    print('prime number')
else:                            # if the count means the factor are more than 2 then num is not a prime number
     print('not a prime number')        