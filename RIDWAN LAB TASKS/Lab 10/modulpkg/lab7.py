# Rectangle class
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Square class inherited from Rectangle
class Square(Rectangle):
    def __init__(self, side):
        # Call the parent class constructor with side as both width and height
        super().__init__(side, side)


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __str__(self):
        return f"Point2D({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"
    
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    def distance_from_origin(self):
        r2d = super().distance_from_origin()
        return math.sqrt(r2d ** 2 + self.z ** 2)
    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"