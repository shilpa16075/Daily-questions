# write a program to multiple all the user given numbers.
def multiply(*numbers):
    """This function is for multiplying all the user inputs"""
    total = 1
    for i in numbers:
        # print(f'the multiplication of {i} and {total} is:')
        total *=i
    return total

answer = multiply(1,2,3,4,5)
print(answer)
answer = multiply(2,3,-6,8)
print(answer)
answer = multiply(2,5,8,9,0,6)
print(answer)