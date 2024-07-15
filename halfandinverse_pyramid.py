num = int(input('Enter a number: '))
#normal half pyramid
"""
for i in range(1, num+1):
    for j in range(1,i+1):
        print("*", end = "")
    print()
"""
#inverted half pyramid

for i in range(1, num+1):
    for j in range(1,(num-i)+2):
        print("*", end = "")
    print()
