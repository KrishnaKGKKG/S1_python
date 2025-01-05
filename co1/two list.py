l1,l2=[],[]
n1=int(input("enter size of first list"))
for i in range(n1):
 l1.append(input(f"l1[{i}]:"))
n2= int(input("enter size of second list"))
for i in range(n2):
 l2.append(input(f"l2[{i}]:"))

if l1==l2:
    print("list are equal and are of same length")
else:
    print("list are not equal!")
    if(len(l1)==len(l2)):
       print("list are of same length")
    else:
         print("list are of different length")
    

common=[]
for i in range (len(l1)):
    if l1[i] in l2:
        common.append(l1[i])
if common:
    print("common values in both list:",common)
else:
    print("both list have no commom elements!")
                      
