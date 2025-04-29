arr = [22,33,11,55,66]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    i = j = k =0

    while i < len(left) and j < len(right):
        if left[i]< right[j]:
            arr[k] = left[i]
            i+= 1
        else:
            arr[k] = right[j]
            j+=1
        k += 1

    while i< len(left):
        arr[k] = left[i]
        i+= 1
        k+= 1

    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+= 1

    print(arr)

merge_sort(arr)