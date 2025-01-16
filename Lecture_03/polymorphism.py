from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, r:float):
        self.r = r

    def area(self):
        return pi * (self.r ** 2)

    def circumference(self):
        return 2 * pi * self.r

class Rectangle(Shape):
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def circumference(self):
        return 2 * (self.a + self.b)

class Triangle(Shape):
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def circumference(self):
        return self.a + self.b + self.c
    
class Cilinder():
    def __init__(self, base:Shape, h: float):
        self.base = base
        self.h = h
    
    def volume(self):
        return self.base.area() * self.h
    
    def surface(self):
        return 2 * self.base.area() + self.base.circumference() * self.h
    
    def edgeLength(self):
        return self.base.circumference() * 2  + self.h * 4
    
c = Circle(3)

korAlapuCililder = Cilinder(c, 5)

print(korAlapuCililder.volume())
