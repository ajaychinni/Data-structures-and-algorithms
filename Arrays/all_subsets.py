def subset (lst):
    set_ = set()
    lst1 = []
    set_.add('')
    for i in range(len(lst)):
        temp = set_.copy()
        for ele in temp:
            set_.add(lst[i])
            set_.add(ele+lst[i])
    return set_

lst = ['1','2','3','4']
print(subset(lst))