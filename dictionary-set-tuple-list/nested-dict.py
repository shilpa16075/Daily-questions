# An introduction of nested dictionary.
# nested dictionary 
student_data = {
    "jenny" : {'marks': 78, 'age':20, 'subject':'pythno'},
    "harry" : {'marks': 95, 'age':21, 'subject':'wed designing'},
    "Aarti" : {'marks': 67, 'age':20, 'subject': 'software design'}
}
print(student_data['harry']['subject'])       # access the specific data
student_data['jenny']['email'] ='jenny123@gmail.com'   # to update the data
print(student_data['jenny'])
del student_data['jenny']['email']   #delete the data
print(student_data['jenny'])
student_data['harry']['email'] = 'harry67@gmail.com'
print(student_data['harry'])
print(student_data['harry'].pop('email'))     #pop fuction
print(student_data)
