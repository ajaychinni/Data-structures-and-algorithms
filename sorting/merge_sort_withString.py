# merge sort with string elements
def merge(array1 , array2):
  i = 0
  j = 0
  result = []
  while i < len(array1) and j < len(array2):
    if len(array1[i]) == len(array2[j]):
      if array1[i] < array2[j]:
        result.append(array1[i])
        i+=1
      else:
        result.append(array2[j])
        j+=1
    elif len(array1[i]) < len(array2[j]):
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

def merge_sort(array):
  if len(array) <= 1 :
    return array
  first = 0
  last = len(array) - 1
  mid = (first + last) // 2
  left = merge_sort(array[:mid + 1])
  right = merge_sort(array[mid + 1:])
  res = merge(left,right)
  return res


print(merge_sort(['301','4','20']))
