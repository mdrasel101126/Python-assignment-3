
class User:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.account_number="".join(name.split())+email
        self.loan_limit=2

    def deposit(self,amount):
        if amount<0:
            print("Please Enter Valid Amount")
            return
        self.balance+=amount
        print(f"Deposit {amount} is successfull!")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Withdrawal amount exceeded")
            return
        self.balance-=amount
        print(f"Withdrawal {amount} is successfull!")
    
    def check_balance(self):
        print(f"Available Balance: {self.balance}")
    
    def transaction_history(self):
        pass

    def take_loan(self,amount):
        pass
    
    def transfer(self):
        pass

    
    def __repr__(self):
        return f" Name: {self.name}\n Email: {self.email}\n Address: {self.address}\n Account Type: {self.account_type}\n Balance:{self.balance}\n Account Number: {self.account_number}"
    
