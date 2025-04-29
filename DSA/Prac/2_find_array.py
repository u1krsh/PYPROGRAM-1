def find_arr(arr,find):
    n,m = len(arr),len(find)

    for i in range(n):
        if arr[i:i+n] == find:
            return True
    return False

arr = ["a","x","a","b","c"]
find= ["a","b","c"]
print(find_arr(arr,find))