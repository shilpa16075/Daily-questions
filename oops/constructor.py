class student:
    # class attribute which are common for ever object
    college_name = "Shri ram college"
    def __init__(self,fullname,marks,college):       # fullname = given parameter  #you can add more arguments like marks course etc
        self.name = fullname   # object attribute
        self.marks = marks
        self.college_name = college 
           # object attribute are non common attributes
           #self.name =  new name created in object
        print('adding new student in database')

s1= student('shilon',45,"shri ram" )
print(s1.name,s1.marks)
print(s1.college_name)

s2 = student('divyansh',39,'dav')
print(s2.name,s2.marks)

s3 = student('shilpa',47,'mdu')
print(s1.name,s1.marks,s1.college_name)