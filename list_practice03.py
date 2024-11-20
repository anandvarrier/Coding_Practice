"""
List Practice
Write a Python program to multiply all the items in a list.
"""

# Function to multiply all the elements in the list
def mul_list_ele(numm):
    mul = 1
    for i in numm:
        mul *= i
    return mul

mul_inpt = list(map(int, input('Enter numbers: ').split()))

print(mul_list_ele(mul_inpt))
