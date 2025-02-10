#Mon Jan 27 18:01:16 2025

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
o = str(input("Ennter Option(+,-,*,/,%,//): "))

if(o=="+"):
    print(f"{a}+{b} = {a+b}")
elif(o=="-"):
    print(f"{a}-{b} = {a-b}")
elif(o=="*"):
    print(f"{a}*{b} = {a*b}")
elif(b!=0):
    if(o=="/"):
        print(f"{a}/{b} = {a/b}")
    elif(o=="%"):
        print(f"{a}%{b} = {a%b}")
    elif(o=="//"):
        print(f"{a}//{b} = {a//b}")
    else:
        print("Invalid Input")
else:
    print("0 Error")