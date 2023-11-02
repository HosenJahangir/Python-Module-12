import random
from datetime import datetime
currentDateAndTime = datetime.now()


class Bank:

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.balance = 0
        self.loan_feature = True
        self.total_loan = 0
        self.users = []
        self.admin = {}

    def create_account(self, user):
        self.users.append(user)

    def delete_account(self, account_number):
        for user in self.users:
            if user.ac_num == account_number:
                self.users.remove(user)
                print('Account has been deleted')

    def show_users(self):
        for user in self.users:
            print(f'{user.name}-{user.email}-{user.ac_num}')

    def total_balance(self):
        print(self.balance)

    def total_loan_amount(self):
        print(self.total_loan)

    def offLoan_onLoan(self, status):
        if status == 'on':
            self.loan_feature = True
        elif status == 'off':
            self.loan_feature = False


class User:
    def __init__(self, name, password, email, address, account_type) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.ac_num = random.randint(100, 999)
        self.transaction_his = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def availabale_balance(self):
        print(self.balance)

    def take_loan(self, amount):
        if self.loan < 2:
            self.balance += amount
            self.loan += 1

        else:
            print('Number of laon exceded')

    def trans_amt(self, amount):
        self.balance -= amount


class Transaction:
    def __init__(self, type, balance) -> None:
        self.time = currentDateAndTime.strftime("%H:%M:%S")
        self.description = type
        self.balance = balance
