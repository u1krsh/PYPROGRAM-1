arr = [22,33,11,55,66]

def binary_seach(arr,target):
    left = 0
    right =len(arr)-1
    while left <= right:
        middle = len(arr) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle-1
    return -1

binary_seach(arr,22)