# Write a Python program to print all even numbers from 1 to 20.

#Approach 1
a = []
for i in range(1,21):
    if i%2 == 0:
        a.append(i)
    else:
        print('...')
print(a)

#Approach 2
for i in range(2, 21, 2):
  print(i)
