#Mon Jan 27 18:43:27 2025


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
o = input("Enter Option (+, -, *, /): ")

if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/' and b != 0:
    print(a / b)
else:
    print("Invalid Input or Division by Zero")
