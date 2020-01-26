# find the pairs where i<j<n and  a[i] < a[j]
import math
def count_pairs(arr,k):
    arr.sort()
    high = len(arr)-1
    low = 0
    while high > low:
        m = math.ceil((high +low) / 2)
        if k > arr[len(arr)-1]:
            return len(arr)
        if k >arr[len(arr)-2]:
            return len(arr)-1
        elif arr[m] == k or (arr[m-1] < k and arr[m+1] >= k):
            if arr[m] < k:
                return len(arr[:m]) + 1
            return len(arr[:m])
        elif arr[m] < k:
            low = m + 1
        else :
            high = m - 1
    if high == 0:
        return 0
    return len(arr)

def find_pair(lst):
    temp = []
    total_sum = 0
    for i in range(len(lst)):
        temp  = lst[i+1:]
        c = count_pairs(temp,lst[i])
        total_sum+=c
    return total_sum
print(find_pair([10,2,3,4,1,5,13,23,10,11,16]))
