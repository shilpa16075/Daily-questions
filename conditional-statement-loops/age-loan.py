# Check eligiblity for loan based on age and income.
age = int(input('Enter your age: '))
# if age>=18 and income>=50000:
#     print('You are eligible!!!')
# else:
#     print('You are not eligible!!!!!')

if age>=18:
    income = int(input('Enter your income: '))
    if income>=50000:
        print('You are eligible!!!')
    else:
        print("Your income is low!!!")
else:
    print('Your age is not suitable')
