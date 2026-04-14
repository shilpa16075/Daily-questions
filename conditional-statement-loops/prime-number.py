# Check if the number is prime number or not.
num = int(input('enter the number of your choice: '))
count= 0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count == 2:
    print('prime number')
else:
     print('not a prime number')        