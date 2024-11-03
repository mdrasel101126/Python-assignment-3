
class Bank:
    def __init__(self,name,initial_balance):
        self.name=name
        self.initial_balance=initial_balance
        self.total_balance=initial_balance
        self.total_loan=0
        self.users=[]
        self.admins=[]
        self.is_loan_feature_on=True

    def add_user(self,user):
        self.users.append(user)

    def user_list(self):
        if len(self.users)==0:
            print("No User!")
        else:
            for user in self.users:
                print(user)
                print()

    def delete_user(self,user):
        pass

    def check_total_balance(self):
        print(f"Available Balance: {self.total_balance}")

    def check_total_loan(self):
        print(f"Total Loan: {self.total_loan}")
    
    def on_loan_feature(self):
        self.is_loan_feature_on=True

    def off_loan_feature(self):
        self.is_loan_feature_on=False

    def add_balance(self,amount):
        self.total_balance+=amount
    
    def add_loan(self,amount):
        self.total_loan+=amount
        self.total_balance-=amount

    def withdraw(self,amount):
        self.total_balance-=amount