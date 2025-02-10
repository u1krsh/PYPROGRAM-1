x = int(input("Enter Temperature: "))

if x > 30:
    print("Its Hot")
elif x >20 and x < 30:
    print("Nice weather")
elif x >10 and x <19:
    print("Cool weather")
elif x <10:
    print("Its Cold")
else:
    print("Invalid Temperature")