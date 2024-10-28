# Calculate the factorial of a given number.

def factorial(n):
    if n == 0 or n == 1:
         return 1
    else:
        return n * factorial(n-1)

#print('Factorial of {} is: ',format(num),factorial(num))
num = int(input('Enter a number: '))
print('Factorial of {} is: '.format(num),factorial(num))
