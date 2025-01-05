n=int(input("enter:\n1 to add\n2 to substract\n3 to multiply\n4 to divide\n"))
a,b=int(input("enter number 1:")),int(input("enter number 2:"))

if n==1:
    print(a+b)
elif n==2:
    print(a-b)
elif n==3:
    print(a*b)
elif n==4:
    print(a/b)
else:
    print("invalid input!")
