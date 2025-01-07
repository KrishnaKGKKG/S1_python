class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):   
        return self.length * self.breadth
    def perimeter(self):  
        return 2 * (self.length + self.breadth)
        
        
l1=int(input("enter length of first rectangle:"))
l2=int(input("enter length of second rectangle:")) 
b1=int(input("enter breadth of first rectangle:"))
b2=int(input("enter breadth of second rectangle:"))
    
r1 = rectangle(l1, b1)
r2 = rectangle(l2, b2)
    
print(f"area of first rectangle is {r1.area()}")
print(f"area of second rectangle is {r2.area()}")
    
if r1.area()>r2.area():
        print("area of first rectangle is greater")
elif r1.area()<r2.area():
        print("area of second rectangle is greater")
else:
       print("area of both rectangles are equal")
        