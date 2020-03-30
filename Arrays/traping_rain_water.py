#Brute force approch
# calculate left and right largest tower and use arr [min(right,left) - current]
def find_max(lst):
	maxs = 0
	for i in lst:
		if i > maxs:
			maxs = i
	return maxs

def calculate(lst):
	total = 0
	for i in range(len(lst)):
		#Skip first and last tower no water can be traped by it
		if i == 0 or i == len(lst) -1:
			continue
		# find left max tower 
		left = find_max(lst[:i+1])
		# find nearby right max tower
		right  = find_max(lst[i:])
		# calculate amount of water on top of this
		total += min(left,right) - lst[i]
	return total

lst = [3,0,0,2,0,4]
print("total",calculate(lst))




