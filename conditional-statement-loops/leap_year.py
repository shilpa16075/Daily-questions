# check if the year is leap year or not
a = int(input('Enter the year you want to check:  '))
if((a%400==0 )or (a%4==0) and a%100!=0 ):
    print('leap year: ')
else: 
    print('not a leap year')