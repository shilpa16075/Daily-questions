# An introduction of nested dictionary.
# nested dictionary 
student_data = {
    "jenny" : {'marks': 78, 'age':20, 'subject':'pythno'},
    "harry" : {'marks': 95, 'age':21, 'subject':'wed designing'},
    "Aarti" : {'marks': 67, 'age':20, 'subject': 'software design'},
    "failed": ['mohan','tripti','gaurav','sandeep']
}
# access the specific data
print(student_data['harry']['subject']) 

 # to update the data
student_data['jenny']['email'] ='jenny123@gmail.com'  
print(student_data['jenny'])

#delete the data
del student_data['jenny']['email']   
print(student_data['jenny'])

#pop fuction
student_data['harry']['email'] = 'harry67@gmail.com'
print(student_data['harry'])
print(student_data['harry'].pop('email'))     
print(student_data)
# list in a nested dictionary
print(student_data['failed'])
# accessing the list index
print(student_data['failed'][0])
