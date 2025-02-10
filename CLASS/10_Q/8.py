x = int(input("Enter Number: "))

if x > 1 and x<7:
    if x == 2:
        print("Monday")
    elif x == 3:
        print("Tuesday")
    elif x == 4:
        print("Wednesday")
    elif x == 5:
        print("Thursday")
    elif x == 6:
        print("Friday")
    else:
        print("Saturday")
else:
    print("Invalid day number")