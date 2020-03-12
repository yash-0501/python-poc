class c1:
    def m1(self):
        print("in C1 - m1")

class c2(c1):
    def m1(self):
        print("In c2 - m1") #this m1 overrides m1 of c1
    
obj1 = c1()
obj2 = c2()

obj2.m1()