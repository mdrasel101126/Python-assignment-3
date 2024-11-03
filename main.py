from bank import Bank
from user import User
from admin import Admin


bank=Bank("Baper Bank",50000)
""" user1=User("Ashik Voja","ashik@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user1)
user2=User("Juel Rana","juel@gmail.com","Sylhet, Bangladesh","Saving")
bank.add_user(user2)

user2.deposit(bank,500)
user2.withdraw(bank,50)
user2.take_loan(bank,5000)

bank.user_list()

user2.transfer(bank,"AshikVojaashik@gmail.com",60)
bank.user_list()
user2.check_transaction_history()

bank.delete_user("AshikVojaashik@gmail.com")
bank.user_list() """


while True:
    print("Welcome To National Fake Bank!")
    print("Options")
    print("\t1. Login as a User\n\t2. Login as an Admin\n\t3. Exit")
    option=int(input("Enter: "))

    user=None

    if option==1:
        while True:
            print("Options:")
            print("\t1. Create Account\n\t2. Deposit\n\t3. Withdraw\n\t4. Check Balance\n\t5. Check Transaction History\n\t6. Take Loan\n\t7. Transfer\n\t8. Exit")
            opt=int(input("Enter: "))
            if opt==1:
                name=input("Enter Name: ")
                email=input("Enter Email: ")
                address=input("Enter Address: ")
                account_type=input("Enter Account Type: ")
                user=User(name,email,address,account_type)
                bank.add_user(user)
                print("----User Created Successfully----")
            elif opt==2:
                amount=int(input("Enter Amount: "))
                user.deposit(bank,amount)
            elif opt==3:
                amount=int(input("Enter Amount: "))
                user.withdraw(bank,amount)
            elif opt==4:
                user.check_balance()
            elif opt==5:
                user.check_transaction_history()
            elif opt==6:
                amount=int(input("Enter Amount: "))
                user.take_loan(bank,amount)
            elif opt==7:
                acc_no=input("Enter Receiver Account Number: ")
                amount=int(input("Enter Amount: "))
                user.transfer(bank,acc_no,amount)
            elif opt==8:
                break
            else:
                continue

                




