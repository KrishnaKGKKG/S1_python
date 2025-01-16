import csv

csv_file="prgm3.txt"

with open(csv_file,'r') as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)
