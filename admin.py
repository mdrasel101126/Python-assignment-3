
class Admin:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
    
    def user_list(self,bank):
        if len(bank.users)==0:
            print("No User!")
        else:
            for user in bank.users:
                print(user)
                print()
    
    def delete_user(self,bank,account_number):
        user=next((user for user in bank.users if user.account_number==account_number),None)
        if user is None:
            print("User Not Found!")
            return
        bank.users.remove(user)
        print("User Removed Successfully!")

    def check_total_balance(self,bank):
        print(f"Available Balance: {bank.total_balance}")
    
    def check_total_loan(self,bank):
        print(f"Total Loan: {bank.total_loan}")

    def on_loan_feature(self,bank):
        bank.is_loan_feature_on=True
        print("Loan Feature is Turned On!")

    def off_loan_feature(self,bank):
        bank.is_loan_feature_on=False
        print("Loan Feature is Turned Off!")

    def on_bankrupt(self,bank):
        bank.is_bankrupt=True
        print("The bank is Bankrupt From Now")

    def off_bankrupt(self,bank):
        bank.is_bankrupt=False
        print("The bank is Running From Now")