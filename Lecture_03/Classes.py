from abc import ABC, abstractmethod
class shapes(ABC):                      #created shapes class which will inherit from ABC class (Abstract classes cannot be instantted)
    def __init__ (self):                # this is a constructor ( this function will run, when a a new instance is created)
        pass
    @abstractmethod
    def area(self)->float:              #every shape must have an area function
        pass
    @abstractmethod
    def circ(self)->float:
        pass

class rect(shapes):                   # let rectangle be a shape 
    def __init__(self, a:float, b:float):     # constructor , we save its arguments
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