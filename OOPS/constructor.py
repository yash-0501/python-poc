class Computer:
    
    def __init__(self):
        self.name = "Raj"
        self.age = 24
    
    def update(self):   #self refers to current object
        self.age = 24
    def compare(self,other):
        if(self.age==other.age):
            return True
        else:
            return False
            
#constructor
c1 = Computer() #c1 refers to obj
c2 = Computer() #c2 refers to obj

c1.name,c1.age="Ravi",20
print(c1.name)
print(c1.age)
print(c2.name) 
print(c2.age)

# c1.update() 
print("Updated Age of c1:",c1.age)

if c1.compare(c2):
    print("Same Age")
else:
    print("Different Age")

#different obj different addresses
#size of object depends upon the no of variables used
