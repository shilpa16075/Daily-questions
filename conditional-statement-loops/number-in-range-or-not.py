# Check if the number is in given range or not.
start_value =int(input('Enter the starting range value: '))
end_value = int(input('Enter the ending range value: '))
num = int(input('Enter the value you want to check: '))
if start_value<=num<=end_value:
    print('Number is in range')
else:
    print('Number is out of range')
