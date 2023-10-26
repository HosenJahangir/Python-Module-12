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

admin = Admin('Admin Officer')
admin.user_list()
admin.total_bank_balance()
admin.see_total_loan()
admin.loan_on_off('on')
user2.take_loan(10000)

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
            pass
        elif admin_choice == 2:
            pass
        elif admin_choice == 3:
            pass
        elif admin_choice == 4:
            admin.total_bank_balance()
        elif admin_choice == 5:
            admin.see_total_loan()
        elif admin_choice == 6:
            pass
    elif choice == 2:
        print('1. Deposit amount')
        print('2. Withdraw amount')
        print('3. Check available balance')
        print('4. Check transaction history')
        print('5. Take loan')
        print('6. Transfer the amount to others account')
        user_choice = int(input('Select an option from avobe 6: '))
    elif choice == 3:
        break
