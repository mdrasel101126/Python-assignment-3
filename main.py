from bank import Bank
from user import User
from admin import Admin


bank=Bank("Baper Bank",50000)
user=User("Ashik Voja","ashik@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user)
user=User("Juel Rana","juel@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user)


bank.user_list()