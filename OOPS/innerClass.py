class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class Laptop:  #class inside a class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Yash',45)
s2 = Student('Yashi',46)


s1.show()

lap1 = s1.lap
lap2 = s2.lap
# print(lap1)