
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

    def find_user_by_email(self,email):
        user=next((user for user in self.users if user.email==email),None)
        return user
    def find_admin_by_email(self,email):
        admin=next((admin for admin in self.admins if admin.email==email),None)
        return admin