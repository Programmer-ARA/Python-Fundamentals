# Methods are the "function that belongs to objects".

class Student:
    College_name = "Galgotias College of Engineering and Tehnology" # Class Attribute

    def __init__(self, name, marks):
        self.name = name # Object Attribute
        self.marks = marks
    
    def greet(self):
        print("(❁´◡`❁) Hey,", self.name)

    def Get_marks(self):
        return self.marks

s1 = Student("Abdur", 98)

s1.greet()
print("College Name :   ",s1.College_name)
print("Name :   ", s1.name)
print("Mark :   ",s1.Get_marks())

s2 = Student("ARA", 100)
s2.greet()
print("College Name :   ",s1.College_name)
print("Name :   ", s1.name)
print("Mark :   ",s1.Get_marks())
