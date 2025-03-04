nums =[8,1,2,2,3]
temp = sorted(nums)
dick = {}
for i,j in enumerate(temp):
    if j not in dick:
     dick[j] = i

res = []
for i in nums:
    res.append(dick[i])
print(res)
