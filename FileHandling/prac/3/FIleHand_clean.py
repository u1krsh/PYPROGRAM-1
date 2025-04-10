try:
    with open("report.txt", "r") as rpr, open("backup.txt", "w") as bkp :
        # r = rpr.readline()
        for i in rpr:
            if i.strip():
                bkp.writelines(i)
        print("File cleaned and written")
except FileNotFoundError:
    print("File not found")
