x = int(input("Enter Number of numbers: "))
y = []
for i in range(0,x+1):
    c = int(input("Enter Number: "))
    y.append(c)
print(min(y))