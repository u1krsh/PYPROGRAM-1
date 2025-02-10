#Sat Jan 25 17:40:57 2025

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Thrid Number: "))

if(a>b&a>c):
    print(a,"is largest")
elif(b>c):
    print(b,"is largest")
else:
    print(c,"is largest")