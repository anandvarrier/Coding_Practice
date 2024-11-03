"""
Write a Python program to create a class that represents a shape.
Include methods to calculate its area and perimeter.
Implement subclasses for different shapes like circle, triangle, and square.
"""


import math


class Shape:
    def cal_area(self):
        pass

    def cal_peri(self):
        pass

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * self.radius ** 2

    def cal_peri(self):
        return 2 * math.pi * self.radius

circle = Circle(3)
c_area = circle.cal_area()
c_peri = circle.cal_peri()

print("Area of the circle: ",c_area)
print("Perimeter of the circle: ",c_peri)

print("=====")

#Rectangle

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def cal_area(self):
        return self.length * self.height

    def cal_peri(self):
        return 2 * (self.length + self.height)

rect = Rectangle(3,2)
r_area = rect.cal_area()
r_peri = rect.cal_peri()

print("Area of rectangle: ",r_area)
print("Perimeter of the rectangle: ",r_peri)


print("=====")

#Triangle

class Triangle(Shape):
    def __init__(self, b1, h1, s1, s2, s3):
        self.b1 = b1
        self.h1 = h1
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def cal_area(self):
        return 0.5 * self.b1 * self.h1

    def cal_peri(self):
        return self.s1 + self.s2 + self.s3

tri = Triangle(4, 7, 3, 4, 5)
t_area = tri.cal_area()
t_peri = tri.cal_peri()

print("Area of a triangle: ",t_area)
print("Perimeter of a triangle: ",t_peri)

print("=====")

#Square

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
    def cal_area(self):
        return self.length ** 2

    def cal_peri(self):
        return 4 * self.length


sq = Square(2)
s_area = sq.cal_area()
s_peri = sq.cal_peri()

print("Area of square: ",s_area)
print("Perimeter of square: ",s_peri)
