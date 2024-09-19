def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lower_bound = [x for x in arr[1:] if x < pivot]
    upper_bound = [x for x in arr[1:] if x >= pivot]
    return quick(lower_bound) + [pivot] + quick(upper_bound)


array = [83, 3, 5, 1, 7, 4]
array = quick(array)
print(array)


# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     lower_bound = [x for x in arr[1:] if x < pivot]
#     upper_bound = [x for x in arr[1:] if x >= pivot]
#     return quick(lower_bound) + [pivot] + quick(upper_bound)
#
# array = [83, 3, 5, 1, 7, 4]
# array = quick(array)
# print(array)
