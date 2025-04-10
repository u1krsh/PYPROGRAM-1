try:
    with open("report.txt", "r") as rep , open("backup.txt", "w") as bcp:
        r = rep.readline()
        while r:
            bcp.write(r)
            r = rep.readline()
        print("Backup Successful")
except FileNotFoundError:
        print("Report.txt does not exist")

