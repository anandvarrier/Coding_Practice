# Find the largest among three numbers entered by the user.
#1st Approach
num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
num3 = int(input('Enter num3: '))

res = max(num1, num2, num3)
print(res)

#2nd Approcah
if num1>num2 and num1>num3:
    print('{num1} is greater than other 2 numbers')
elif num2>num1 and num2>num3:
    print(f'{num2} is greater than other 2 numbers')
else:
    print(f'{num3} is greater than other 2 numbers')
