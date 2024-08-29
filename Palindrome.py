print('Hi')
n = input('Enter a number: ').strip()
print("\nThis script will ask for a number from the user and check weather the number is palindrome ir not")


"""
Pseudo code
n and reverse of n should be same
rev_n = n[::-1]
if n == rev_n
    then a palindrome
else
    not a palindrome
"""
#m = 'anand'
rev_n = n[::-1]

if n == rev_n:
    print('A Palindrome')
else:
    print('Not a palindrome')

#rev_m = m[::-1]
#print(rev_n)
#print(rev_m)
