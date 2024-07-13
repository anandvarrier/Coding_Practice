# The program will print a full pyramid

user=int(input('Enter the layers of pyramid: '))

for i in range(1,user+1):
    #for leading spaces
    for j in range(user-i):
        print(" ", end ="")
    #for printing stars
    for k in range(1,2*i):
        print("*", end="")
    print()
