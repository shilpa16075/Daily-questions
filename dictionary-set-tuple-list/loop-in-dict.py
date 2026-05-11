# Loop in dictionary.
student = {
    "Name":'Shristi',
    "Grade":2,
    "Roll no":13
}
student['Subject'] = "Python"
student['Performance'] = "Excellent"
print(student)
for i in student:
    print(i)      # Accessing key 
    print(student[i])  # Accesing key pair