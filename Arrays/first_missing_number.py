def find_num(lst):
	#preprocesing is converting all negeative number to 1 and all elements larger than n to 1
	lst,flag = preprocessing(lst)
	if flag == True:
		return 1
	n = len(lst)
	#loop to mark all elements present in the array
	for i in lst:
		i = abs(i)
		#as we don't have n index we are using zero th index for that
		if i == n:
			lst[0] = -lst[0]
			continue
		lst[i] = abs(lst[i])
		lst[i] = -lst[i]
	#looping to find out which number is not marked
	for j in range(1,len(lst)):
		if lst[j] < 0 :
			continue
		else:
			# this element is not marked
			return j
	if lst[0] > 0:
	#if zero th index is not marked n is missing
		return n
	#if none were marked eg 1,2,3 return 4
	return n+1

def preprocessing(lst):
	#flag to check if 1 exists in lst or not if not exist just return 1 as missing
	flag = True
	n = len(lst)
	for i in range(len(lst)):
		if lst[i] == 1:
			flag = False
		elif lst[i] < 0 or lst[i] > n: 
			lst[i] = 1
	return lst,flag

print(find_num([-1,-2,3,1]))

0