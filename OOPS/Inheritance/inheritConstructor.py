class class1:
    def __init__(self):
        print("In class 1 init")
    def m1(self):
        print("In class 1")

class class2(class1):
    def __init__(self):
        super().__init__() #calls init of class 1
        print("In class 2 init")
    def m2(self):
        print("In class 2")

obj = class1()
obj = class2() #it also calls constructor of class 1
# if it doesn't have it's init