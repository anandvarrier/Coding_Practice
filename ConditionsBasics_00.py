# If-else-elif blocks
"""
Python does not have switch statements. If-else and elif covers it all.
"""

# Comparisons:
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identity: is

# and
# or
# not

# Example 01
language = "Java"

if language == "Python":
    print('Language is Python')
elif language == "Java":
    print('Language is Java')
else:
    print('No match')

# Example 02
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Wrong credentials!')
