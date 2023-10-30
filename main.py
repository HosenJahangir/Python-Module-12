from bank import Bank, User, Admin

bank = Bank('City Bank', 'Uttara')
user1 = User('Hosen jahangir', 'hosen.jahangir@gmail.com',
             'Espoo', 'Savings')
user2 = User('Anwar Vai', 'anwar.vai@gmail.com', 'Dhaka', 'Current')
bank.users.append(user1)
bank.users.append(user2)

user1.deposit(500)
print(user1.balance)
user1.withdraw(600)
print(user1.balance)
print(bank.balance)
user1.availabale_balance()
user1.take_loan(100)
print(user1.balance)
user1.take_loan(50)
print(user1.balance)
user1.take_loan(20)
print(user1.balance)
user1.take_loan(10)
print(user1.balance)
print(user1.ac_num)

# admin = Admin('Admin Officer')
user2.take_loan(10000)

# Replica
while True:
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    choice = int(input("Select an option: "))
    if choice == 1:
        print('1. Create an account')
        print('2. Delete user account')
        print('3. See User account list')
        print('4. check the total available balance of the bank')
        print('5. check the total loan amount')
        print('6. on or off the loan feature of the bank')
        admin_choice = int(input("Select an option from avaove six: "))
        if admin_choice == 1:
            admin_name = input('Provide name: ')
            admin = Admin(admin_name)
            bank.admin = admin

        elif admin_choice == 2:
            Ac_num = int(input('Provide account number: '))
            for user in bank.users:
                if user.ac_num == Ac_num:
                    bank.users.remove(user)
                    print('Account has been deleted')

        elif admin_choice == 3:
            for user in bank.users:
                print(f'{user.name}-{user.email}-{user.ac_num}')

        elif admin_choice == 4:
            print(bank.balance)

        elif admin_choice == 5:
            print(bank.total_loan)

        elif admin_choice == 6:
            status = input('on/off')
            if status == 'on':
                bank.loan_feature = True
            elif status == 'off':
                bank.loan_feature = False

    elif choice == 2:
        print('1. Deposit amount')
        print('2. Withdraw amount')
        print('3. Check available balance')
        print('4. Check transaction history')
        print('5. Take loan')
        print('6. Transfer the amount to others account')
        user_choice = int(input('Select an option from avobe 6: '))
        if user_choice == 1:
            amount = int(input("Amount : "))
            user1.deposit(amount)
            bank.balance += amount
        elif user_choice == 2:
            amount = int(input("Amount : "))
            user1.withdraw(amount)
            bank.balance -= amount
        elif user_choice == 3:
            user1.availabale_balance
        elif user_choice == 4:
            pass

        elif user_choice == 5:
            if Bank.loan_feature == True:
                amount = int(input("Amount : "))
                user1.take_loan(amount)
                bank.total_loan += amount
            else:
                print('Currently Bank is not giving loan')

    elif choice == 3:
        break
