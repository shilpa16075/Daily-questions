# write a program to check whether the given year is leap year or not using if elif else.
year = int(input("enter year: "))
if year%100==0 :
    if year%400==0:
        print('leap year')
    else: 
        print("not leap year")
elif year%4==0:
    print('leap year')
else:
    print("not a leap year")