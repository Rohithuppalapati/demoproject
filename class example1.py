# Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
from math import *

class Circle():
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        r=int(self.radius)
        return pi*(r**2)

    def getCircumference(self):
        r=int(self.radius)
        return 4*pi*(r**2)

c1=Circle(5)
c2=Circle(6)
print(c1.getArea())
print(c1.getCircumference())

