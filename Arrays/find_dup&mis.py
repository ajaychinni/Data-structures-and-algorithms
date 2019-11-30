# find duplicates and missing number from a array in o(n) time and space
def cal(lst,indx):
    n = len(lst)
    lst = map(abs,lst)
    total = sum(lst)
    return int((((n * (n + 1)) / 2)) - (total - indx))

def find_dup(lst):
  cnt = 0
  n  = len(lst)
  for ele in lst:
    indx = abs(ele)

    if indx < len(lst):
      if lst[indx] > 0:
        lst[indx] = lst[indx] * (-1)
      else:
        return indx,cal(lst,indx)
    else:
        if lst[0] < 0:
            return indx,cal(lst,indx)
        lst[0] = lst[0] * (-1)

  if cnt == 2:
    return indx,cal(lst,indx)

print(find_dup([4,3,2,3]))
