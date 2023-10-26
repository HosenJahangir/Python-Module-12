import random


class Bank:
    balance = 0
    users = []
    total_loan = 0
    loan_feature = True

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.ac_num = random.randint(100, 999)

    def deposit(self, amount):
        self.balance += amount
        Bank.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            Bank.balance -= amount
        else:
            print('Withdrawal amount exceeded')

    def availabale_balance(self):
        print(self.balance)

    def take_loan(self, amount):
        if Bank.loan_feature == True:
            if self.loan < 2:
                self.balance += amount
                self.loan += 1
                Bank.total_loan += amount

            else:
                print('Number of laon exceded')
        else:
            print('Currently Bank is not giving loan')

    def trans_amt(self, amount):

        self.balance -= amount


class Admin:
    def __init__(self, name) -> None:
        self.name = name

    def create_account():
        pass

    def delete_account():
        pass

    def user_list(self):
        for user in Bank.users:
            print(f'{user.name}-{user.email}')

    def total_bank_balance(self):
        print(Bank.balance)

    def see_total_loan(self):
        print(Bank.total_loan)

    def loan_on_off(self, status):
        if status == 'on':
            Bank.loan_feature = True
        elif status == 'off':
            Bank.loan_feature = False
