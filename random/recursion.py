import sys

# print(sys.getrecursionlimit())

sys.setrecursionlimit(10)

def greet():   #infinite recursion -- 1000 lines(default)
    print("Hello")
    greet()

greet()