
from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
class Rectangle(Shape):
    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b
    def area(self):
        return (self.l*self.b)
        
circle=Circle(radius=int(input("Enter the radius :")))
print(f"Radius of the circle {circle.area()}")

rectangle=Rectangle(l=int(input("Enter the length :")),b=int(input("Enter the breath :")))
print(f" Area of Rectangle : {rectangle.area()}") 