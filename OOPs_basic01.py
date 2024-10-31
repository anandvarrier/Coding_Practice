"""
Write a Python program to create a class representing a Circle.
Include methods to calculate its area and perimeter.
"""
import math

class Cir:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return math.pi * self.radius ** 2

    def cal_peri(self):
        return 2 * math.pi * self.radius


circle = Cir(3)

area = circle.cal_area()

peri = circle.cal_peri()

print('Area of circle is: ', area)

print('Perimeter of circle is: ', peri)
