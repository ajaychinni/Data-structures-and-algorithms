def subarray(lst,k):
	lst = sorted(lst)
	p1 = 0
	p2 = 0
	sums = 0
	lst_all = []
	while p2 < len(lst):
		if sums < k:
			sums += lst[p2]
			p2+=1
		elif sums > k:
			sums -=lst[p1]
			p1+=1
		else:
			lst1 = [lst[i] for i in range(p1,p2)]
			lst_all.append(lst1)
			sums += lst[p2]
			p2+=1
	return lst_all




print(subarray([4,3,2,1,6,8],6))
