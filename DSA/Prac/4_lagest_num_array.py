def larges_arr(arr):
    largest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
        else:
            continue

    return largest

x = [1,2,3,4,5,6,7,8,9]
print(larges_arr(x))