# dictionary in a list 
student_data =[
    {
        'name':'ram',
        'age':17,
        'class':'12th',
        'marks':89
        },
    {
        'name':'sohan',
        'age':18,
        'class':'12th',
        'marks' :94,
        'phone no':[12452417,52365252]
        },
    {
        'name':'rishi',
     'age':17,
     'class':'12th'
     ,'marks':87
     }
]
print(student_data[0])
print(type(student_data))
print(student_data[1]['phone no'])  # list in dict 