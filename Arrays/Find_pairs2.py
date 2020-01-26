# find the pairs where i<j<n and  a[i] < a[j]

import math
def count_pairs(arr1,arr2):
    result = []
    i = 0
    j = 0
    count = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            count+=1
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    while i < len(arr1):
        result.append(arr1[i])
        i+=1
    while j < len(arr2):
        result.append(arr2[j])
        j+=1
    return result,count

def find_pair(lst):
    if len(lst) <= 1:
        return lst
    h = len(lst)-1
    l  = 0
    m = (h+l)//2

    left,count = find_pair(lst[:m+1])
    right,count = find_pair(lst[m+1:])
    result,count=count_pairs(left,right)
    # count+=count

    return result,count

print(find_pair([10,2,3,4,1,5,13,23,10,11,16]))
