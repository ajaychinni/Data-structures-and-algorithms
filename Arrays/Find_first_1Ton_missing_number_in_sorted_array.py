#finding first mising value from a sorted array where the miising value should be 1 to n (duplicates, negative are allowed)
def find_mising_value(lst):
  i = 0
  j = 1
  while j < len(lst):
    diff  = lst[j] - lst[i]
    if diff == 1:
      i+=1
      j+=1
    else:
      return lst[i] + 1
  return lst[i]+1
print(find_mising_value([0,1,2,3,4,5,6,7]))
