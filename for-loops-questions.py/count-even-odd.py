# Write a python program to count the number of even and odd numbers from the series.
list_num = [1,3,2,45,6,74]
even = 0
odd = 0
for i in list_num:
    if i %2==0:
        even+=1
    else:
        odd+=1
print('total even no in series are:',even)
print('total odd number in series are:',odd)