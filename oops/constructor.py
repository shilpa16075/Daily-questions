class student:
    # class attribute which are common for ever object
    college_name = "Shri ram college"
    def __init__(self,fullname,marks):       # fullname = given parameter  #you can add more arguments like marks course etc
        self.name = fullname   # object attribute
        self.marks = marks    # object attribute are non common attributes
           #self.name =  new name created in object
        print('adding new student in database')

s1= student('shilon',45)
print(s1.name,s1.marks)
print(s1.college_name)

s2 = student('divyansh',39)
print(s2.name,s2.marks)