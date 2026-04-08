class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Marks: {self.marks}")

# Object banana
s1 = Student("Aryan", 85)
s1.display()