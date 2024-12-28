import math

class Shape:
    def area():
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
val1 = Circle(2)
val2 = Rectangle(2,2)
print(val1.area())
print(val2.area())
