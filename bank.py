
class Bank:
    def __init__(self,name,initial_balance):
        self.name=name
        self.initial_balance=initial_balance
        self.total_balance=initial_balance
        self.total_loan=0
        self.users=[]
        self.admins=[]
        self.is_loan_feature_on=True
        self.is_bankrupt=False

    def add_user(self,user):
        self.users.append(user)

    def add_admin(self,admin):
        self.admins.append(admin)

    def user_list(self):
        if len(self.users)==0:
            print("No User!")
        else:
            for user in self.users:
                print(user)
                print()

    def delete_user(self,account_number):
        user=next((user for user in self.users if user.account_number==account_number),None)
        if user is None:
            print("User Not Found!")
            return
        self.users.remove(user)
        print("User Removed Successfully!")

    def check_total_balance(self):
        print(f"Available Balance: {self.total_balance}")

    def check_total_loan(self):
        print(f"Total Loan: {self.total_loan}")
    
    def on_loan_feature(self):
        self.is_loan_feature_on=True
        print("Loan Feature is Turned On!")

    def off_loan_feature(self):
        self.is_loan_feature_on=False
        print("Loan Feature is Turned Off!")

    def on_bankrupt(self):
        self.is_bankrupt=True
        print("The bank is Bankrupt From Now")
    def off_bankrupt(self):
        self.is_bankrupt=False
        print("The bank is Running From Now")

    def find_user_by_email(self,email):
        user=next((user for user in self.users if user.email==email),None)
        return user
    def find_admin_by_email(self,email):
        admin=next((admin for admin in self.admins if admin.email==email),None)
        return admin