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

print(c_area)
print(c_peri)

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

print(r_area)
print(r_peri)
