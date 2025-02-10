x = int(input("Enter Number of Numbers:"))
y = []
for i in range(1, x+1):
    c = int(input("Enter Number: "))
    y.append(c)
    print(y.min())