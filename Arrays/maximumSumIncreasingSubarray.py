def find_sum(arr):
    maxs = 0
    total = arr[0]
    for i in range(len(arr) -1 ):
        if arr[i] < arr[i+1]:
            total +=arr[i+1]
            if maxs < total:
                maxs = total
        else:
            total = arr[i+1]
            print("end")
    return maxs
print(find_sum([2,3,4,22,3,7,9,10,8,9,10,20]))