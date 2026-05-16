class student:

    def __init__(self,fullname):       # fullname = given parameter
        self.name = fullname    #self.name =  new name created in object
        print('adding new student in database')

s1= student('shilon')
print(s1.name)

s2 = student('divyansh')
print(s2.name)