# if-elif-else is used to check multiple conditions in a program. 
# Python exectues the first true conditon and skip the remaining ones.
# if condition:
#   sequence to statement1
# elif condition:
#  sequence to statement2
# else:
#  default statement
# num = int(input("enter your marks: "))
# if num>89:
#     print("Grade A")
# elif num>79:
#     print("Grade B")
# elif num>69:
#     print("Grade C") 
# else :
#     print("The Grade D") 
num = int(input("enter your marks: "))
if num>89:
    letter = 'A'
elif num>79:
    letter = 'B'
elif num>69:
    letter = 'C' 
else :
    letter = 'D'
print("The Grade " , letter)   
 