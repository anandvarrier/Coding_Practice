#WAP to find the missing number in the array

a = [1,2,3,4,5,6,8,9]
"""
#Summation method
#This logic will work only for single missing numbers
def find_missingnum(a):
    n = a[-1]
    print(type(n))
    print(n)
    total = (n*(n+1))//2
    sum1 = sum(a)
    res = total - sum1
    print(res)

find_missingnum(a)

"""
#XOR method
#This logic will work only for single missing numbers

def find_missingXOR(a):
    n=len(a)
    xor_a = a[0]
    for index in range(1,n):
        xor_a=xor_a^a[index]
        print("XOR of ",xor_a ,"and ",a[index], "is", xor_a)
    x2=0
    for index in range(1,n+2):
        x2=x2^index

    print(xor_a^x2)

find_missingXOR(a)

