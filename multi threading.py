from threading import *
from time import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello Rohith')
            sleep(4)

class Hi(Thread):
    def run(self):
        for i in range(6):
            print('Hi Rohith')
            sleep(2)


instance1=Hello()
instance2=Hi()

instance1.start()
sleep(1)
instance2.start()

instance1.join()
instance2.join()

