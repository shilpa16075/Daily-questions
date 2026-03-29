import time
count =int(input("enter the count: "))
print("/n countdown start now: ")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("happy birthday!!!")