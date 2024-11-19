"""
List Comprehension Practice
Count the number of spaces in a string
"""

#Traditional Loop Method
s = 'I am a Software Developer. '
num = []
for space in s:
    if ' ' in space:
        num.append(' ')
print(len(num))

print('####')

#LC Method

num = [' ' for space in s if ' ' in space]
print(len(num))


