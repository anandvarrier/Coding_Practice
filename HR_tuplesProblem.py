n = int(input('Enter n: '))

numbers = list(map(int, input('Enter nums: ').split()))
print(numbers)
t = tuple(numbers)
print(t)
print(hash(t))
