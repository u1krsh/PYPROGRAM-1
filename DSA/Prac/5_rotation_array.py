def rot_arr(arr):
    inv_index = len(arr) -1
    fwd_index = 0
    while fwd_index < inv_index:
        arr[fwd_index] , arr[inv_index] = arr[inv_index] , arr[fwd_index]
        fwd_index += 1
        inv_index -= 1
    return arr

arr = [1,2,3,4,5]
print(rot_arr(arr))