class A: #Superclass
    def feat1(self):
        print("Feature 1")
    
    def feat2(self):
        print("Feature 2")

#Child Class / Subclass
class B(A):    #Class B inherits all the Objects of A
    def feat3(self):
        print("Feature 3")
    
    def feat4(self):
        print("Feature 4")

#Multilevel Inheritance
class C(B):    #Class C inherits all the Objects of B
    def feat5(self):
        print("Feature 5")

#Multiple Inheritance
class D():    
    def feat6(self):
        print("Feature 6")
class E(C,D):
    def feat7(self):
        print("Feature 7")

a1 = A()
a1.feat1()
a1.feat2()

b1=B()
b1.feat3()
b1.feat2()

c1=C()
c1.feat5()
c1.feat3()
c1.feat1()

d1=D()
d1.feat6()

e1=E()
e1.feat6()
e1.feat5()