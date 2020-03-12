#Poly - Many
#Morph - Form

#Objects have multiple forms

class PyCharm:
    def execute(self):
        print("Py Charm -- Compiling")
        print("Running")

class VSC:
    def execute(self):
        print("VS Code -- Compiling")
        print("Running")
        print("This is better")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = VSC()

obj = Laptop()
obj.code(ide)

ide = PyCharm()
obj.code(ide)