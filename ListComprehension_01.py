# Python list Comprehension

"""
Find all of the numbers from 1-1000 that are divisible by 7
"""
"""
# Traditional for loop
num = []

for i in range(1,1001):
    if i % 7 == 0:
        num.append(i)
print(num)
"""


#List Comprehension
num = [i for i in range(1,1001) if i % 8 == 0]
print(num)

