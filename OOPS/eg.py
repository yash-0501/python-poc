class Computer:
    #Attributes -> Variables
    #Behaviours -> Methods

    def config(self):
        print("i7, 16gb, 250GB")
    
comp = Computer() #constructor
print(type(comp))

comp2 = Computer()
#int,str,float etc -- all are classes

Computer.config(comp) #to call method inside a class
Computer.config(comp2) 

# ============
comp.config() #config takes comp1 as an arg
comp2.config()

