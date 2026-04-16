# Check if the triangle is valid on not, if yes then find the type of triangle.
# Equilateral / Isosceles / Scalene batana
a = int(input('Enter the angle of a triangle: '))
b = int(input('Enter the angle of a triangle: '))
c = int(input('Enter the angle of a triangle: '))
if a+b+c==180:
  print('This is a triangle')
  if a==b==c:
    print(f'Equilateral triangle with angle {a}')
  elif a==b or b==c or a==c:
    print(f'Isosceles triangle with angles {a}, {b}, {c}')
  else:
    print(f'Scalene triangle with angles {a} ,{b},{c}')
else:
  print('Not a triangle')