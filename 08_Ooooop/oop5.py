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
    

