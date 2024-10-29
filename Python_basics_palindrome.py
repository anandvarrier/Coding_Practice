# Write a Python program to check if a given string is a palindrome.

user_str = input('Enter a string: ')
if user_str == user_str[::-1]:
    print('Palindrome')
else:
    print('Not a Palindrome')
