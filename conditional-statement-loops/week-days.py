# Display the days of the week for a given numbers.
day_num = int(input('Enter the day number you want to check: '))
if day_num==1:
    print('Moday')
elif day_num==2:
    print('Tuesday')
elif day_num==3:
    print('Wednesday')
elif day_num==4:
    print('Thursday')
elif day_num==5:
    print('Friday')
elif day_num==6:
    print('Saturday')
elif day_num==7:
    print('Sunday')
else:
    print('Invalid Number!!!!!')

# Second method
day_name = int(input('enter the day you want to check: ')) 
match day_name:
    case 1:
        print('Moday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:  
        print('Thursday')      
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7: 
        print('Sunday')   
