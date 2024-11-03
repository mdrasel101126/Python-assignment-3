from bank import Bank
from user import User
from admin import Admin


bank=Bank("Baper Bank",50000)
user1=User("Ashik Voja","ashik@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user1)
user2=User("Juel Rana","juel@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user2)

user2.deposit(bank,500)
user2.withdraw(bank,50)

bank.check_total_balance()
bank.user_list()