# Learning basic funtions of a String
#name = input('Enter your name: ')
# phno = input('Enter a phone number: ')

#r = len(name) # returns total length of a string including spaces
#r = name.find('a') # returns the position of the first occurence of character
#r = name.rfind('a')
    #rfind()-reverse find: returns the position of the occurence of character but from the reverse end.
    #if the charecter is not found, it reterns -1.
#r = name.capitalize() # returns a string where the first letter of each word is capital
#r = name.upper() # returns a string with all charaters in capitals
#r = name.lower() # returns a string with all charaters lower
#r = name.isdigit() # returns True if only a digit is found in the string otherwise False
#r = name.isaplha() # returns True if only alphabets are found in the string otherwise False
#r = phno.count('-') # counts the total number of the provided element in the string
#r = phno.replace("-"," ") 

# print(r)


# Exercise:
"""
Validate user input
1) username is no more than 12 characters
2) username must not contain spaces
3) username must not contain digits
"""

uname = input('Enter username: ')
if len(uname)>12:
    print('Username cannot be more than 12 characters')
elif not uname.find(" ") == -1:
    print('Username cannot contain spaces.')
elif not uname.isalpha() :
    print('Username cannot contain digits.')
else:
    print('All 3 conditions cleared!')
    
