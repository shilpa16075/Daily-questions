# list basics 
n = int(input("enter a number: "))
number_list = []
for i in range(n):
    a = int(input("enter values for the list: "))
    number_list.insert(i,a)
print("entered list",number_list)