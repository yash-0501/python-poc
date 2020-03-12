#big tasks into small parts - parts->threads

from threading import *
from time import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello") #ob1 thread
            sleep(0.5)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi") #ob2 thread
            sleep(0.5)



ob1 = hello()
ob2 = hi()

ob1.start()
sleep(0.2)
ob2.start()
ob1.join() # wait for ob1 thread to join
ob2.join() # wait for ob2 thread to join
print("Bye") #main thread
#by default every execution has main thread