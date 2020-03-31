def find_triplets(lst,target):
    n = len(lst)
    s = set()
    lst.sort()

    for i in range(0,n-2):
        left = i+1
        right = n-1
        while (right > left):
            if lst[i] + lst[right] +lst[left] == target:
                s.add((lst[i],lst[right],lst[left]))
                right -=1
            elif lst[i] + lst[right] +lst[left] < target:
                left +=1
            else:
                right -=1
    return s
                    
print(find_triplets([1,2,3,4,4,4,5,6],9))
        