from abc import ABC, abstractmethod

class Computer(ABC): #class having abstract methods
    @abstractmethod #decorator
    def process(self):
        pass #abstract method -with declaration no definition


#cannot create an object of abstract classes

class Laptop(Computer): #can't be instantiated w/o any method since it has abstract method
    def process(self):
        print("Works")

# ob = Computer()
ob1 = Laptop()
ob1.process()