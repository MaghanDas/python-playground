from abc import ABC, abstractmethod

# Pillar - 3 : Polymorphism

class Shape(ABC):

    @abstractmethod
    def area(self)-> float:
        """Calculate the area of the shape"""
    
    @abstractmethod
    def perimeter(self)-> float:
        """Calculate the perimeter of the shape"""
    
    def describe(self)-> str:
        # this uses the child's area(): polymorphism in action.
        return f"{self.__class__.__name__} has an area of {self.area()} and a perimeter of {self.perimeter()}"
    

class Circle(Shape):
    def __init__(self,radius:float):
        self.radius = radius
    
    def area(self)->float:
        import math 
        return math.pi * self.radius ** 2
    
    def perimeter(self)-> float:
        import math 
        return 2 * math.pi * self.radius 
    
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width 
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self)-> float:
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = self.perimeter() / 2        # Heron's formula
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    def perimeter(self) -> float:
        return self.a + self.b + self.c

# polymorphism- same functions works on any shape.
def print_shape_info(shape:Shape)->None:
    print(shape.describe())
    
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]


for shape in shapes:
    print_shape_info(shape)   # works for ALL without if/elif chains