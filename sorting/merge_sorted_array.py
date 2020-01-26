def custom_sort(arr):
    key = arr[0]
    j = 1
    while j < len(arr) and arr[j] < key:
        arr[j-1] = arr[j]
        j+=1
    arr[j-1] = key
    return arr 
def merge_arr(arr1, arr2):
    i = 0
    j = 0
    while i < len(arr1):
        if arr1[i] <= arr2[j]:
            i+=1
        else:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            if j < len(arr2)-1 and arr2[j] > arr2[j + 1]:
                arr2 = custom_sort(arr2)
    return arr1,arr2
arr1 = [1,2,3,7,9]
arr2 = [1,4,6,8]
print(merge_arr(arr1,arr2))