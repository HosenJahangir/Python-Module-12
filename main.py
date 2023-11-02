from bank import Bank, User, Transaction

bank = Bank('City Bank', 'Uttara')

# Replica
while True:
    print("1. Admin Login")
    print("2. User Login")
    print("3. Exit")
    choice = int(input("Select an option: "))
    if choice == 1:
        while True:
            print('1. Create an account')
            print('2. Delete user account')
            print('3. See User account list')
            print('4. check the total available balance of the bank')
            print('5. check the total loan amount')
            print('6. on or off the loan feature of the bank')
            print('7. Back')
            admin_choice = int(input("Select an option from avaove six: "))
            if admin_choice == 1:
                account_name = input('Acount name: ')
                password = int(input('Passward: '))
                email = input('Acount email: ')
                address = input('Acount address: ')
                account_type = input('Acount type: ')
                user = User(account_name, password,
                            email, address, account_type)
                bank.create_account(user)

            elif admin_choice == 2:
                Ac_num = int(input('Provide account number: '))
                bank.delete_account(Ac_num)

            elif admin_choice == 3:
                bank.show_users()

            elif admin_choice == 4:
                bank.total_balance()

            elif admin_choice == 5:
                bank.total_loan_amount()

            elif admin_choice == 6:
                status = input("Input 'on/off'")
                bank.offLoan_onLoan(status)

            elif admin_choice == 7:
                break

    elif choice == 2:
        bank_user = {}
        name = input("Name: ")
        password = int(input("Password: "))
        flag = 1
        for user in bank.users:
            if user.name == name and user.password == password:
                bank_user = user
                flag = 0
        if flag:
            print("Invalid email or password")
            continue
        while True:
            print('1. Deposit amount')
            print('2. Withdraw amount')
            print('3. Check available balance')
            print('4. Check transaction history')
            print('5. Take loan')
            print('6. Transfer the amount to others account')
            print('7. Back')
            user_choice = int(input('Select an option from avobe 6: '))
            if user_choice == 1:
                amount = int(input("Amount : "))
                bank_user.deposit(amount)
                bank.balance += amount
                transaction = Transaction("Deposit", bank_user.balance)
                bank_user.transaction_his.append(transaction)
            elif user_choice == 2:
                amount = int(input("Amount : "))
                if bank_user.balance >= amount:
                    if bank.balance >= amount:
                        bank_user.withdraw(amount)
                        bank_user.balance -= amount
                        transaction = Transaction("Withdraw", bank.balance)
                        bank_user.transaction_his.append(transaction)
                    else:
                        print("Bank is bankrupt")
                else:
                    print('Withdrawal amount exceeded')
            elif user_choice == 3:
                bank_user.availabale_balance()
            elif user_choice == 4:
                for transaction in bank_user.transaction_his:
                    print(
                        f"Time: {transaction.time}, Type: {transaction.description}, Balance: {transaction.balance}")

            elif user_choice == 5:
                if bank.loan_feature == True:
                    amount = int(input("Amount : "))
                    bank_user.take_loan(amount)
                    bank.total_loan += amount
                    transaction = Transaction("Loan", bank_user.balance)
                    bank_user.transaction_his.append(transaction)
                else:
                    print('Currently Bank is not giving loan')
            elif user_choice == 6:
                account_number = int(input("Account Number: "))
                amount = int(input("Amount: "))
                flag = 1
                for user in bank.users:
                    if user.ac_num == account_number:
                        if bank_user.balance >= amount:
                            bank_user.trans_amt(amount)
                            user.balance += amount
                            transaction = Transaction(
                                "Transfer", bank_user.balance)
                            bank_user.transaction_his.append(transaction)
                            flag = 0
                        else:
                            print("Insufficient balance")
                            flag = 0
                if flag:
                    print("Account number doesn't match")

            elif user_choice == 7:
                break

    elif choice == 3:
        break
