#abstract class is a class that cannot be instantiated and 
# is meant to be subclassed. It can contain abstract methods, 
# which are methods that are declared but not implemented in the
#  abstract class. Subclasses of the abstract class must implement
#  the abstract methods.
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.base + self.height + (self.base**2 + self.height**2)**0.5

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4)]# This will raise a TypeError because we cannot instantiate an abstract class
s2=shape()#type error 
s3= Circle()#
print(s3.area())
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    print(f"The perimeter of the {shape.__class__.__name__} is: {shape.perimeter()}")