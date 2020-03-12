class car:
    #static var
    wheels = 4 #class variable same for all objs

    def __init__(self):
        #instance variables - diff for diff objs
        self.mil=10  
        self.com="BMW"


c1 = car()
c2 = car()

c1.mil=8
car.wheels=5 #since it exists in class namespace
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
