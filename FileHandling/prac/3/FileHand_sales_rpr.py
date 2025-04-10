import csv

with open("sales.csv", "r") as file:
    sales = {}
    x =csv.reader(file)
    next(x)
    for row in x:
        product,price,quan = row[0], float(row[1]),int(row[2])
        sales[product] = price*quan
    print(sales)