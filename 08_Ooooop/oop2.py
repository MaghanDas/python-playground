# 🔹 4. Methods in OOP
# Methods are functions defined inside a class that can access and modify the attributes of the class or perform other actions.
# Instance Methods:
# These methods operate on an instance (object) of the class and typically modify or access the object's attributes.
# Class Methods:
# These methods are bound to the class and not the instance. They take the class itself as their first argument (cls).
# Use @classmethod decorator to define a class method.
# Static Methods:
# Static methods don't have access to the instance (self) or the class (cls). 
# They work like regular functions but are included in the class for organization. Use @staticmethod decorator.

class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        return f"Driving {self.make} {self.model}!"

    @classmethod
    def get_wheels(cls):
        return cls.wheels

    @staticmethod
    def  car_info():
        return "Cars are vehicles with four wheels."

# Instance method
car1 = Car("Toyota", "Camry")
print(car1.drive())  # Output: Driving Toyota Camry!

# Class method
print(Car.get_wheels())  # Output: 4

# Static method
print(Car.car_info())  # Output: Cars are vehicles with four wheels.