def dupes(lst):
    x = []
    for i in range(len(lst)):
        for j in range (i + 1, len(lst)):
                if lst[i] == lst[j]:
                    x.append(lst[j])       
    return x

print(dupes([1,1,2,3,4,5,4,5]))
        