"""Create a list of number from 1to 100 and print only even numbers from that list. (in just 2 lines)
"""

numbers = list(range(0,101))
print([num for num in numbers if num % 2 ==0])
