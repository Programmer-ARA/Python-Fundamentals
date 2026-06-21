# ABSTRACTION:- Hiding the implementation details of class and only showing the essential features to the user.
# ENCAPSULATION:- Wrapping data and functions into a single unit (object).


class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Class Started")

Car1 = Car()

Car1.start()