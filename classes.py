class Person:
    species = "Homosapien"

    def hello(self):
        print ("Hello  World")

    def __init__ (self, name , age):
        self.name = name
        self.age = age

    def  hi(self):
        print("hi my name is "+ self.name)


class Teacher(Person):
    role = "teacher"

    def hi (self):
        print("Hi my name is Mx. " + self.name)

Forlenza = Teacher("Forlenza", 184)
print(Forlenza.role)

Forlenza.hi()

class Student(Person):
    role = "Student"


Bryant = Student("Bryant", 17)
print(Bryant.name)
print(Bryant.age)
Bryant.hi()


Wesley = Student("Wesley",99)
print(Wesley.name)
print(Wesley.age)


Students = Student("Students" , 185)
print(Students.role)

Students.hi()