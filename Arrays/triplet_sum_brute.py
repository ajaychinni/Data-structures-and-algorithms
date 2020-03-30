def find_triplets(lst,target):
    n = len(lst)
    s = set()
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if lst[i]+lst[j]+lst[k] == target:
                    s.add((lst[i],lst[j],lst[k]))
    return s
                    

print(find_triplets([1,2,3,4,5,6],9))
        