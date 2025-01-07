class bankaccount:
    def __init__(self,accountno,name,account_type,balance):
        self.accountno=accountno
        self.name=name
        self.account_type=account_type
        self.balance=balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"Rs{amount} successfully deposited")
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance")
            return
        else:
            self.balance-=amount
            print(f"Rs{amount} successfully withdrawed")
    def display(self):
        print(f"account number:{self.accountno}\naccount holder name:{self.name})\naccount type:{self.account_type}\naccount balance:{self.balance}")

accountno1=int(input("enter account number:"))
name1=(input("enter account holder name:"))
account_type1=(input("enter account type:"))

account1=bankaccount(accountno1,name1,account_type1,0)

while True:
    print("\n\n\n")
    account1.display()
    transaction=int(input("enter 1 to deposit\nenter 2 to withdraw"))
    amount=int(input("enter amount:"))
    if(transaction==1):
        account1.deposit(amount)
    elif(transaction==2):  
        account1.withdraw(amount)
    else:
        print("invalid choice!")
