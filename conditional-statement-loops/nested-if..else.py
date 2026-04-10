# nested if...else
num = int(input("enter the number: "))
if num>0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    if num%2==0:
        print("negative even")
    else:
        print("negative odd")