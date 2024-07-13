#the program will print downward stairs pattern

user=int(input('Enter the layers of pyramid: '))

for i in range(1, user+1):
    for k in range(user-i):
        print("",end="")
    for j in range(1,2*i):
        print("*", end="")
    print()

