from datetime import datetime
class User:
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.account_number="".join(name.split())+email
        self.loan_limit=2
        self.transaction_history=[]

    def deposit(self,bank,amount):
        if amount<0:
            print("Please Enter Valid Amount")
            return
        self.balance+=amount
        bank.total_balance+=amount
        message=f"Deposit {amount} is successfull! Date: {datetime.now()}"
        self.transaction_history.append(message)
        print(f"Deposit {amount} is successfull!")
    
    def withdraw(self,bank,amount):
        if amount>self.balance:
            print("Withdrawal amount exceeded")
            return
        elif amount>bank.total_balance:
            print("The Bank is Bankrupt!!!")
            return
        self.balance-=amount
        bank.total_balance-=amount
        message=f"Withdrawal {amount} is successfull! Date: {datetime.now()}"
        self.transaction_history.append(message)
        print(f"Withdrawal {amount} is successfull!")
    
    def check_balance(self):
        print(f"Available Balance: {self.balance}")
    
    def check_transaction_history(self):
        if len(self.transaction_history)==0:
            print("No Transaction History!")
        else:
            for history in self.transaction_history:
                print(history)

    def take_loan(self,bank,amount):
        if bank.is_loan_feature_on is False:
            print("Sorry! Bank Could Not Provide Loan At This Moment")
            return
        if self.loan_limit==0:
            print("Sorry! Loan Limit Finished")
            return
        if bank.total_balance<amount:
            print("Sorry No Available Money!")
            return
        self.balance+=amount
        self.loan_limit-=1
        bank.total_balance-=amount
        bank.total_loan+=amount
        message=f"Loan {amount} is Successfull! Date: {datetime.now()}"
        self.transaction_history.append(message)
        print(f"Loan {amount} is Successfull!")
    
    def transfer(self):
        pass

    
    def __repr__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance:{self.balance}\nAccount Number: {self.account_number}"
    
