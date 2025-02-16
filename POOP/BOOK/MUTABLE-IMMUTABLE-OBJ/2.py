def sumi(lst):
    x = []
    for j in range(len(lst)):
        for i in range(j + 1, len(lst)):
            x.append(lst[i] + lst[j])
    return x

print(sumi([1,2,3,4,5,6]))