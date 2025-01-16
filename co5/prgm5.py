import csv

data=[
    {"name":"jacku","age":3,"gender":"male"},
    {"name":"jaani","age":4,"gender":"female"},
    {"name":"jillu","age":1,"gender":"male"}
]

csv_file="prgm.csv"

with open(csv_file,'w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=["name","age","gender"])
    writer.writeheader()
    writer.writerows(data)

with open(csv_file,'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
