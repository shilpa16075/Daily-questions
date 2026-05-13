
student_data = [ 
    {
        'name':'ram',
    'course':'bca',
    'subject':'python',
    'roll no' : 18
    },
    {
        'name':'sita',
        'course':'bcom',
        'subject':'accounts',
        'roll no': 14
    }
]
def add_new_student(name,course,subject,roll_no):
    new_student={}
    new_student['name']=name
    new_student['course']=course
    new_student['subject']=subject
    new_student['roll no']=roll_no
    student_data.append(new_student)
    

add_new_student('shyam','ba','geography',15)
print(student_data)


