x = [1,2,3,4,6,8]
myiter = iter(x)
# print(next(myiter))
# print(next(myiter)) 
for i in range(0, len(x)):
    print(myiter.__next__())