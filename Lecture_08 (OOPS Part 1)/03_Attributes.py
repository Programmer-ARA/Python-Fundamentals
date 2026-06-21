# There are two types of attributes:
# 1. Class Attribute            2. Instance or Object Attribute

class Student:
    College_name = "Galgotias College of engineering and tehnology" # Class Attribute

    def __init__(self, name, marks):
        self.name = name # Object Attribute
        self.marks = marks

s1 = Student("Abdur", 98)
print(s1.name)
print(s1.College_name)
