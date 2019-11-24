#binary search with recursion
def bin_search(first,last,target,lst):
    if first > last:
        return -1
    mid = (first + last) // 2

    if lst[mid] == target:
        return mid

    elif lst[mid] < target:
        return bin_search(mid+1,last,target,lst)
    else:
        return bin_search(first,mid - 1,target,lst)

print(bin_search(0,len([2,3,5,8,9])-1,5,[2,3,5,8,9]))
