class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def demo(self):
        print(self.name,self.age)
p1 = person('shilpa',20)
p1.demo()