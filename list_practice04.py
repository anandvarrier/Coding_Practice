"""
List Practice:
Write a Python program to get the largest number from a list.
Pseudo Code:

Go through each element in the list.
Compare 1st element with the 2nd and so on a so fourth.
When you get the largest element, print it.

"""

numm = [5,9,3,14,5]

def largest(numm):
    maxx = numm[0]
    for i in numm:
        if i > maxx:
            maxx = i
    return maxx

#===

def largest_inbuilt(numm):
    num = max(numm)
    return num

print(largest_inbuilt(numm))


