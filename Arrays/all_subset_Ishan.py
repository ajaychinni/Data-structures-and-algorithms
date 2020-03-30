def power_set(array):
    if len(array) < 1:
        return []
    result = [[]]
    for item in array:
        sub_set = [something + [item] for something in result]
        result.extend(sub_set)
    return result
print(power_set([2,3,4,5]))