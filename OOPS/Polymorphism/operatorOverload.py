class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

       

s1 = Student(58,69)
s2 = Student(83,49)

s3=s1+s2   #overloaded __add__

print(s3.m1)
print(s1)