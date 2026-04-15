# Check if the triangle is valid or not.
angle1 = int(input('enter the angle1: '))
angle2 = int(input('enter the angle2: '))
angle3 = int(input('enter the angle3: '))
if angle1+angle2+angle3 ==180:
    print('triangle is valid')
else:
    print('triangle is not valid')
# second method
if angle1>0 and angle2>0 and angle3>0 and angle1+angle2+angle3==180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')