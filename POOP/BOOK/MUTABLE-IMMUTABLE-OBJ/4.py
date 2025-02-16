def lstt(n):
    x = []
    for i in range(1,n+1):
        for j in range(1,5+1):
            x.append(i*j)
            
    return x

print(lstt(5))