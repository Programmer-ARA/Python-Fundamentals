# # ----------- QUESTION - 01 -----------
# Create a student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def Get_average(self):
#         self.average = ((self.m1 + self.m2 + self.m3)/3)
#         return self.average
    
# s1 = Student("Abdur", 76, 97, 100)

# print(s1.name, s1.m1, s1.m2, s1.m3)
# print(s1.Get_average())


# Accesing marks in list

class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def Get_average(self):
        sum =0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "Your Average Mark is", sum/3)

s1 = Students("Abdur", [67, 89, 100])
s1.Get_average()