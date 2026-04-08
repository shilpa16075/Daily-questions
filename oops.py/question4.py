class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof! Woof!")

my_dog = Dog()
my_dog.speak()  # Output: Dog says: Woof! Woof!