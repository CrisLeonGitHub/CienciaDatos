import csv

with open("0. datos\\data.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)