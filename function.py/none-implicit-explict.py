# The return Statement: If omitted, a function implicitly returns None.
# implicitly return: where python internally assume to return 'nothing or none'
def simple_function():
    print("output stream operation..")
result = simple_function()
print(result)
# explicitly return : when the function returns a value 
def check_none1(a,b):
    return a+b
output = check_none1(3,5)
print(output)
