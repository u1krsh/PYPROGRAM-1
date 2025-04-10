try:
    with open("report.txt", "r") as rpr:
        r = rpr.read()
    r = r.replace("mode=debug","mode=production")
    with open("report.txt", "w") as rpr:
        rpr.write(r)
except FileNotFoundError:
    print("File not found")
