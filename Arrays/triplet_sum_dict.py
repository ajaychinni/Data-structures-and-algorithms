def remove (ele1,d):
    temp = dict(d)
    for k in d.keys():
        if ele1 > k:
            del temp[k]
    if ele1 in d:
        if temp[ele1] == 1:
            del temp[ele1]
        else:
            temp[ele1]-=1

    return temp
def find_triplets(lst,target):
    #storing values in dict
    d = {}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    #iteration O(n^2)
    s = set()
    n = len(lst)
    for i in range(0,n-1):
        for j in range(i+1,n):
            temp_d = remove(lst[i],d)
            temp_d = remove(lst[j],temp_d)
            find_num  = target - (lst[i]+lst[j])
            if find_num in temp_d:
                s.add((lst[i],lst[j],find_num))
    return s
    
print(find_triplets([1,2,3,4,4,4,5,6],9))