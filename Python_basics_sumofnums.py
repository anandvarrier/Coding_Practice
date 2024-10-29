# Calculate the sum of all numbers from 1 to a given number.

# Approach 1
n = int(input('Enter a number: '))
summ = 0
for i in range(1,n+1):
    summ=summ+i
print(summ)

print('*******')

#Approach 2
sum_result = sum(range(1, n + 1))
print("Sum:", sum_result)
