class student:

    def __init__(self,fullname,marks):       # fullname = given parameter  #you can add more arguments like marks course etc
        self.name = fullname 
        self.marks = marks
           #self.name =  new name created in object
        print('adding new student in database')

s1= student('shilon',45)
print(s1.name,s1.marks)

s2 = student('divyansh',39)
print(s2.name,s2.marks)