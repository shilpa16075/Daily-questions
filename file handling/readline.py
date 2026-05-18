# more about reading a file.
file = open('demo.txt','r')
# data = file.read(11)
# print(data)
data1 = file.readline()        # To print one line
print(data1)
data2 = file.readline()       # To print second line
print(data2)
file.close()