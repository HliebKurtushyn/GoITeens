from math import pi

class Shape:
    def calculate_area(self, a, b):
        ...

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


area_rectangle = Rectangle(10, 15).calculate_area()
area_circle = Circle(10).calculate_area()

print(f"Rectangle: {area_rectangle}\nCircle: {area_circle:.2f}")