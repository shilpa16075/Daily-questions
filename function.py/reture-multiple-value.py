# Write a function calculation() that accepts two variables and calculates both addition and subtraction.
#  The function must return both results in a single return statement.
def calculation(a,b):
    c = a+b
    d = a-b
    return c,d
sum_result,sub_result = calculation(57,43)
print("addition:",sum_result)
print('subtraction',sub_result)