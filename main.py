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

    if option==1:
        user=None
        while True:
            print("Options:")
            print("\t1. Create Account\n\t2. Deposit\n\t3. Withdraw\n\t4. Check Balance\n\t5. Check Transaction History\n\t6. Take Loan\n\t7. Transfer\n\t8. Exit")
            opt=int(input("Enter Option: "))
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
    elif option==2:
        admin=None
        while True:
            print("Options:")
            print("\t1. Create Account\n\t2. Delete User\n\t3. Check User List\n\t4. Check Available Balance\n\t5. Check Total Loan\n\t6. Turn On Loan Feature\n\t7. Turn Off Loan Feature\n\t8. Set Bankrupt True\n\t9. Set Bankrupt False\n\t10. Exit")
            opt=int(input("Enter Option: "))
            if opt == 1:
                name=input("Enter Name: ")
                password=input("Enter Password: ")
                admin=Admin(name,password)
                bank.add_admin(admin)
                print("Admin Created Successfully")
            elif opt == 2:
                acc_no=input("Enter Account Number: ")
                bank.delete_user(acc_no)
            elif opt==3:
                bank.user_list()
            elif opt==4:
                bank.check_total_balance()
            elif opt==5:
                bank.check_total_loan()
            elif opt==6:
                bank.on_loan_feature()
            elif opt==7:
                bank.off_loan_feature()
            elif opt==8:
                bank.on_bankrupt()
            elif opt==9:
                bank.off_bankrupt()
            elif opt==10:
                break
            else:
                continue
    elif option==3:
        break
    else:
        continue
            

                




