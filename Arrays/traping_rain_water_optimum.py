def precompute(lst):
	maxs  = lst[0]
	precompute_lst = []
	for i in lst:
		if i > maxs:
			maxs = i
		precompute_lst.append(maxs)
	return precompute_lst

def calculate(lst):
	total = 0
	left = precompute(lst[:])
	right  = precompute(lst[::-1])
	for i in range(len(lst)): 
		total += min(left[i],right[i]) - lst[i]
	return total

lst = [3,1,4,3,2,1,4]
print("total",calculate(lst))