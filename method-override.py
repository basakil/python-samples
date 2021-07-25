# Python program to demonstrate
# method overriding


# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self._value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self._value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        super().__init__()      ## unnecessary, actually..
        self._value = "Inside Child"

    # Child's show method
    # def show(self):
    #     print(self.value)


# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

# print(obj1.__dict__['_value'])