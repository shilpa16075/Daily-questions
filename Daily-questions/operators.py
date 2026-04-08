# write a program to take 2 number and perform all the operator.
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
# Arithematic operator
print(a+b)
print(a-b)
print(a*b)
c = a/b
print(c,type(c))
# comparsion operation
print(a<b) #true 23<46
print(a>b) #false 23<46
print(a==b) # false 23==46 not equal
print(a!=b) # true 23!46
print(a<=b) # true 23<=46
print(a>=b) # false 23>=46
# logical operator
print(a<b and a<=b) # true and true then output is true
print(a<b and a>=b) # true and false then output is false
print(a<b or a<=b) # true or true then output is true
print(a<b or a>=b) # true or false then output is false
print(not(a<b) )# reverse the result
# assignment operators
a = a+6 # it is also written as 
print(a)
a+=7
print(a)
a*=10
print(a)