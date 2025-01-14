from abc import ABC, abstractmethod
class shapes(ABC):
    def __init__ (self):
        pass
    def area(self)->float:
        pass
    def circ(self)->float:
        pass

class rect(shapes):
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
    def area(self)->float:
        return (self.a * self.b)
    def circ(self)->float:
        return (self.a *2 + self.b*2)


class tri(shapes):
    def __init__(self, a:float, b:float, m:float):
        self.a = a 
        self.b = b
        self.m = m
    def area(self)->float:
        return (self.a * self.m / 2)
    def circ(self)->float:
        return (self.a+self.b*2)


myRectangle = rect(14, 22)
print("Area is: ", myRectangle.area(), "and the circumfance is: ", myRectangle.circ())

myTri = tri(2, 4, 2)
print ("Area is:", myTri.area(), "and circ is:", myTri.circ())