class Person:
    species = "Homosapien"

    def hello(self):
        print ("Hello  World")

    def __init__ (self, name , age):
        self.name = name
        self.age = age

    def  hi(self):
        print("hi my name is"+ self.name)

Bryant = Person("Bryant", 17)
print(Bryant.name)
print(Bryant.age)
Bryant.hi()


Wesley = Person("Wesley",99)
print(Wesley.name)
print(Wesley.age)
