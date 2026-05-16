class student:

    def __init__(self,fullname):
        self.name = fullname
        print('adding new student in database')

s1= student('shilon')
print(s1.name)

s2 = student('divyansh')
print(s2.name)