#same as above only if array is unsorted
def find_mising_value2 (lst):

  lst2 = [False]*len(lst)
  lst2[0] = True
  for val in lst:
    if val > 0:
      lst2[val] = True

  for i in range(len(lst2)):
    if lst2[i] == False:
      return i

print(find_mising_value2([5,6,7,4,9,2,-5,-4,-7,7,8,0,3,1]))
