class publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"publisher:{self.name}")
        
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print(f"book name :{self.title}\nauthor:{self.author}")
        
        

class python(book) :
    def __init__(self,name,title,author,price,pagesnum):
        super().__init__(name,title,author)
        self.price=price
        self.pagesnum=pagesnum
        
    def display(self) :
        super().display()
        print(f"book price: Rs{self.price}\nnumber of pages:{self.pagesnum}")
        
        
book=python(name="abc",title="def",author="ghi",price="200",pagesnum="100") 
book.display()