# Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates
#  the addition of a and b. The outer function should then add 5 to that sum and return the final result.
def outer(a,b):
    def addition(sum):
        sum = a+b
        # print('sum of a,b is',sum)
        sum1 = sum +5
        return sum,sum1
    addition(sum)

result = print(outer(2,3))


