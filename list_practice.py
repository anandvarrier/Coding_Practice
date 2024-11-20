"""
List Practice
Write a Python program to sum all the items in a list.
"""

num = list(map(int, input('Enter numbers: ').split()))

print(num)

def sum_of_list(num):
    summ = 0
    for i in num:
        summ += i
    return summ

print(sum_of_list(num))





