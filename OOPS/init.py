class student:
    def __init__(self,name,roll): #gets called automatically
        self.name = name
        self.roll = roll   #parameterized constructor

    def std_info(self):
        print("Details:", self.name, self.roll)



std1 = student("Raj",21)
std2 = student("Ravi",22)

std1.std_info()
std2.std_info()