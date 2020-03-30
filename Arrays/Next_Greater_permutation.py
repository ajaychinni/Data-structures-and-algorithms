def greater(lst):
    i = len(lst) -1
    flag = 0
    while i > 0:
        if lst[i] <= lst[i-1]:
            i-=1
        else:
            flag = 1
            min_indx = 0
            lst2 = lst[i:]
            for j in range(len(lst2)):
                if lst2[j] < lst2[min_indx]:
                    if lst2[j] > lst[i-1]:
                        min_indx = j

            min_indxx = min_indx + len(lst[:i])
            lst[min_indxx],lst[i-1] = lst[i-1], lst[min_indxx]
            lst[i:len(lst)] = sorted(lst[i:len(lst)])
            break
    if flag == 0:
        return lst[::-1]
    return lst
print(greater([11,5,7,9,2,2,1]))