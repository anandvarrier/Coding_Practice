#WAP to find out pairs with given sum of value an array
#arr = [5,7,4,3,9,8,19,21]
#sum = 17

def twoSum(arr, trgsum):
    arr.sort()
    #print(arr)
    left = 0
    right = len(arr)-1
    pairs = []
    #print(left)
    #print(right)
    while(left<=right):
        if((arr[left] + arr[right]) > trgsum):
            right=right-1
        elif((arr[left] + arr[right]) < trgsum):
            left=left+1
        elif(arr[left] + arr[right] == trgsum):
            #print('Values of pair are',arr[left],"&", arr[right])
            pairs.append((arr[left],arr[right]))
            #break
            right=right-1
            left=left+1
    print(pairs)
            
arr = [1,2,3,8,7,9,19,4]
trgsum = 5

res = twoSum(arr,trgsum)
