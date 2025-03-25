def merge_sorted(arr1,arr2):
    mer = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mer.append(arr1[i])
            i += 1
        else:
            mer.append(arr2[j])
            j += 1
    return mer 
arr1 = [1,3,5,7]

arr2 = [2,4,6,8]
print(merge_sorted(arr1,arr2))
    