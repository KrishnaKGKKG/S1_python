year=int(input("enter the year"))
current=2025
if year<=current:
    print("invalid year")
else:
    print("leap years are:")
    for i in range(current+3,year,4):
        print(i)
