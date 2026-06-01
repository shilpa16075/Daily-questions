# Basics of dictionary
student_info = {
    "name":"Ram",
    "dept":"uiet",
    "subject" :"cloud computing",
    "age" : 20 
}
print(student_info["dept"])   # finding the values with the help of key


# finding the key with the help of value
for key,value in student_info.items():
    if value =="Ram":
        print(f'The key for the value pair ram is: {key}')