# Fibonacci Numbers Native approach

n = int(input("Enter how many numbers of the fibonacci series you want: "))
n1 = 0
n2 = 1
next_n = n2
count = 1

print(n1,n2, end = " ")
while count<=n:
    print(next_n, end = " ")
    count+=1
    n1, n2 = n2, next_n
    next_n = n1+n2
print()
