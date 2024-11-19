"""
List comprehension practice
Find all of the numbers from 1-1000 that have a 3 in them
"""
#Traditional loop method:
num = []

for i in range(1, 1001):
    if '3' in str(i):
        num.append(i)
print(num)
print(f'There are {len(num)} numbers in which number 3 can be found.')

#----

#List comprehension method:
numlc = [i for i in range(1, 1001) if '3' in str(i)]
print(num)

if num == numlc:
    print('Lists have same elements.')
else:
    print('False')
