def quick_sort(arr):
    if len(arr )<= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr if x <pivot]
    right = [x for x in arr if x>pivot]
    middle = [x for x in arr if x==pivot]

    return quick_sort(left) +quick_sort(middle) + quick_sort(right)

arr = [22,33,11,55,66]
print(quick_sort(arr))