def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        a = arr[:mid]
        b = arr[mid:]
        merge(a)
        merge(b)
        mearge_full(a, b, arr)


def mearge_full(a, b, arr):
    n1 = len(a)
    n2 = len(b)
    i, j, k = 0, 0, 0
    while n1 > i and n2 > j:
        if a[i] > b[j]:
            arr[k] = b[j]
            k += 1
            j += 1
        else:
            arr[k] = a[i]
            k += 1
            i += 1
    while n1 > i:
        arr[k] = a[i]
        k += 1
        i += 1
    while n2 > j:
        arr[k] = b[j]
        j += 1
        k += 1


array = [8, 5, 9, 7, 4, 6, 1, 4, 5]
merge(array)
print(array)


