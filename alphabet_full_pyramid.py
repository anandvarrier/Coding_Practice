alpha = 65
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1, 2*i):
        print(chr(alpha), end="")
        alpha+=1
    alpha= 65
    print()
