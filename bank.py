import random


class Bank:

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.balance = 0
        self.loan_feature = True
        self.total_loan = 0
        self.users = []
        self.admin = {}


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
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
        if amount <= self.balance:
            self.balance -= amount

        else:
            print('Withdrawal amount exceeded')

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


class Admin:
    def __init__(self, name) -> None:
        self.name = name

    def delete_user_account():
        pass
