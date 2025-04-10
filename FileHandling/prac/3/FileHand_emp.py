try:
    x = str(input("Enter empID to remove"))
    with open("backup.txt", "r") as file:
        r = file.readlines()
        with open("backup.txt", "w") as wri:
            for i in r:
                if x not in i:
                        wri.writelines(i)
except FileNotFoundError:
    print("FIle not found")