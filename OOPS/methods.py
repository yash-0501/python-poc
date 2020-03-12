#instance methods -- accessor & mutators
#class methods
#static methods

class Student:

    school = "SPC"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): #self- while working with instance vars
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self): #accessors
        return self.m1

    def set_m1(self,val): #mutators
        self.m1=val
    
    @classmethod
    def get_school(cls): #while working with class var
        return cls.school

    @staticmethod
    def info(): #static method
        print("This is static method")

s1 = Student(45,56,78)
s2 = Student(43,64,87)

print(s1.avg())
print(s2.avg())
print(Student.get_school())
Student.info()

#to fetch -- accessors
#to mutate -- mutators