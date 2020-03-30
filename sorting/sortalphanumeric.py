"""
   Sample Input -> "t9ex8t7709721334AAID"
   Ouput - > "AADIettx01233477789"
"""

def append_ele(lst,i, flag):
  #check if lst empty
  if lst:
      for j in range(len(lst)):
        if lst[j] < i:
          pass
        else:
          flag = 1
          lst = lst[:j] + i + lst[j:]
          break
      # when there is no elemnt in our list greater than the elemnt to be inserted we append that element in the last
      if flag == 0:
        lst  = lst + i
  #add the first element
  else:
    lst  = lst + i
  return lst 
def sort_all(s):
  num = ''
  caps = ''
  lower = ''
  for i in s:
    flag = 0
    if i.isnumeric():
      num  = append_ele(num,i,flag)
    elif i.isupper():
      caps = append_ele(caps,i,flag)
    else:
      lower = append_ele(lower,i,flag)
  return caps+lower+num
 
s = 't9ex8t7709721334AAID'
print(sort_all(s))