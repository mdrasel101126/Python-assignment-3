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
            print("\t0. Login Account\n\t1. Create Account\n\t2. Deposit\n\t3. Withdraw\n\t4. Check Balance\n\t5. Check Transaction History\n\t6. Take Loan\n\t7. Transfer\n\t8. Exit")
            opt=int(input("Enter Option: "))
            if opt==0:
                email=input("Enter Eamil: ")
                password=input("Enter Password: ")
                user=bank.find_user_by_email(email)
                if user is None:
                    print("-----Login Failed! Incorrect Email!-----")
                else:
                    if user.password==password:
                        print("-----Login Successfull!-----")
                        print(f"-----Welcome {user.name}----")
                    else:
                        user=None
                        print("----Incorrect Password----")
            elif opt==1:
                name=input("Enter Name: ")
                email=input("Enter Email: ")
                password=input("Enter Password: ")
                address=input("Enter Address: ")
                account_type=input("Enter Account Type: ")
                user=bank.find_user_by_email(email)
                if user is not None:
                    print("-----User Exist! Please Login-----")
                    continue
                user=User(name,email,password,address,account_type)
                bank.add_user(user)
                print("----User Created Successfully----")
                print(f"-----Welcome {user.name}-----")
            elif opt==2:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                amount=int(input("Enter Amount: "))
                user.deposit(bank,amount)
            elif opt==3:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                amount=int(input("Enter Amount: "))
                user.withdraw(bank,amount)
            elif opt==4:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                user.check_balance()
            elif opt==5:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                user.check_transaction_history()
            elif opt==6:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                amount=int(input("Enter Amount: "))
                user.take_loan(bank,amount)
            elif opt==7:
                if user is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
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
            print("\t0. Login Account\n\t1. Create Account\n\t2. Delete User\n\t3. Check User List\n\t4. Check Available Balance\n\t5. Check Total Loan\n\t6. Turn On Loan Feature\n\t7. Turn Off Loan Feature\n\t8. Set Bankrupt True\n\t9. Set Bankrupt False\n\t10. Exit")
            opt=int(input("Enter Option: "))
            if opt==0:
                email=input("Enter Eamil:")
                password=input("Enter Password: ")
                admin=bank.find_admin_by_email(email)
                if admin is None:
                    print("-----Login Failed! Incorrect Email!-----")
                else:
                    if admin.password==password:
                        print("-----Login Successfull!-----")
                        print(f"-----Welcome {admin.name}-----")
                    else:
                        admin=None
                        print("----Incorrect Password----")
            elif opt == 1:
                name=input("Enter Name: ")
                email=input("Enter Email: ")
                password=input("Enter Password: ")
                admin=bank.find_admin_by_email(email)
                if admin is not None:
                    print("-----Admin Exist! Please Login-----")
                    continue
                admin=Admin(name,email,password)
                bank.add_admin(admin)
                print("----Admin Created Successfully----")
                print(f"-----Welcome {admin.name}-----")
            elif opt == 2:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                acc_no=input("Enter Account Number: ")
                admin.delete_user(bank,acc_no)
            elif opt==3:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.user_list(bank)
            elif opt==4:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.check_total_balance(bank)
            elif opt==5:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.check_total_loan(bank)
            elif opt==6:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.on_loan_feature(bank)
            elif opt==7:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.off_loan_feature(bank)
            elif opt==8:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.on_bankrupt(bank)
            elif opt==9:
                if admin is None:
                    print("-----Pleaase Login or Create Account-----")
                    continue
                admin.off_bankrupt(bank)
            elif opt==10:
                break
            else:
                continue
    elif option==3:
        break
    else:
        continue
            

                




