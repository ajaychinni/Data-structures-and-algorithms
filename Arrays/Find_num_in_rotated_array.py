def find_num(lst,k):
    n = len(lst)
    s = 0
    e = n -1
    while s <= e:
        mid = (s+e) // 2
        if lst[mid] == k:
            return mid 
        elif lst[mid] > lst[s]:
            if lst[mid] > k and lst[s] <= k:
                e = mid - 1
            else:
                s = mid + 1
        else:
            if lst[mid] < k and lst[e] >= k:
                s = mid + 1
            else:
                e = mid - 1
    return False
print(find_num([5,6,7,8,10,1,2,3,4],3))