# STATIC METHODS:- Static Methods are the methods that don't use self as a parameter (Work as class level)

class Student:
    @staticmethod   #decorator

    def hello():
        print("Hello")

s1 = Student()

s1.hello()

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifyinig it/.
