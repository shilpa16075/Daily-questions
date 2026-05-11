student_marks ={
    'Jenny':92,
    'Harry':78,
    'Dimpy':30,
    'Rahul':41,
    'Aniket':99,
    'Prem' : 43
}
def student_grade(data):
    '''This function is called marks grader'''
    marks_grade = {}
    for i,j in data.items():
        if 91<=j<=100:
            grade = "A+"
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        elif 81<=j<=90:
            grade = 'A'
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        elif 71<=j<=80:
            grade = 'B'
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        elif 61<=j<=70:
            grade = 'C'
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        elif 51<=j<=60:
            grade = 'D'
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        elif 41<=j<=50:
            grade = 'E'
            print(f'Student {i} has {grade}')
            marks_grade[i] = grade
        else:
            grade = 'Failed'
            print(f'Student {i} has {grade}')
        marks_grade[i] = grade
    return marks_grade
final_result= student_grade(student_marks)
print(final_result)