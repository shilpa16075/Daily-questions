# check if the year is leap year or not
year = int(input('Enter the year you want to check: '))
if year%4==0 and year%100!=0 or year%400==0:        # century year is not a leap year unless it is divible by 400
    print(f'{year} is a leap year')
else:
    print(f'{year} not a leap year')