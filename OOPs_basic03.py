"""
Write a Python program to create a calculator class.
Include methods for basic arithmetic operations.
"""


class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1 + self.n2

    def subtraction(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        return self.n1 / self.n2

n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))

cal_01 = Calculator(n1, n2)
print('Addition: ', cal_01.addition())
print('Subtraction: ', cal_01.subtraction())
print('Multiplication : ', cal_01.multiplication())
print('Division: ', cal_01.division())
