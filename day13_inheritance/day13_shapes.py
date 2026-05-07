"""
Day 13 - Polymorphism with Shapes
Different shapes, one unified interface.
"""

import math

class Shape:
    """parent class for all shapes"""

    def __init__(self,name):
        self.name=name
    
    def area(self):
        # Parent doesn't know how to calculate area for a generic shape
        # Each child MUST override this
        return 0
    
    def describe(self):
        return f"{self.name} (area: {self.area():.2f})"
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
if __name__ == "__main__":
    # Create a mixed list of shapes
    shapes = [
        Rectangle(5, 3),
        Circle(4),
        Triangle(6, 4),
        Rectangle(2, 2),
        Circle(1),
    ]
    
    # POLYMORPHISM #1: Describe all shapes
    print("📐 All shapes:")
    for s in shapes:
        print(f"  {s.describe()}")
    
    # POLYMORPHISM #2: Math on a mixed list
    total = sum(s.area() for s in shapes)
    print(f"\n📊 Total area of all shapes: {total:.2f}")
    
    # POLYMORPHISM #3: Find the largest shape
    largest = max(shapes, key=lambda s: s.area())
    print(f"🏆 Largest shape: {largest.describe()}")
    
    # POLYMORPHISM #4: Sort by area (smallest to largest)
    sorted_shapes = sorted(shapes, key=lambda s: s.area())
    print(f"\n📋 Shapes sorted by area:")
    for s in sorted_shapes:
        print(f"  {s.describe()}")