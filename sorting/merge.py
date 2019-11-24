#merge Sort
def merge(array1,array2):
  i = 0
  j = 0
  result = []
  while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
      result.append(array1[i])
      i+=1
    else:
      result.append(array2[j])
      j+=1
  while i < len(array1):
    result.append(array1[i])
    i+=1
  while j < len(array2):
    result.append(array2[j])
    j+=1
  return result

def merge_sort(lst):
  if len(lst) <= 1:
    return lst
  start = 0
  last = len(lst) -1
  mid = (start + last) // 2
  left = merge_sort(lst[:mid +1])
  right = merge_sort(lst[mid + 1:])
  result = merge(left,right)
  return result

print(merge_sort([2,4,5,6,7,1,5]))
