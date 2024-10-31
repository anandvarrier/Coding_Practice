"""
Write a Python program to create a person class.
Include attributes like name, country and date of birth.
Implement a method to determine the person's age.
"""

from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def cal_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        return age

person01 = Person('Anand', 'India', date(1998, 2, 12))
person02 = Person('ABC', 'India', date(2000, 12, 2))

age01 = person01.cal_age()
age02 = person02.cal_age()
print(age01)
print(age02)
