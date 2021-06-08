class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance =  balance
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.account_balance < 0:
            print('insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print('Balance:', self.account_balance)
        return self 

    def yeild_interest(self):
        if self.account_balance>0:
            self.int_rate = 0.01
            self.account_balance = self.account_balance * (1+self.int_rate)
        return self

Batou = BankAccount('int_rate', 'balance') 
Major = BankAccount('int_rate', 'balance') 

Batou.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).yeild_interest().display_account_info()

Major.make_deposit(1000).make_deposit(2000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(200).make_withdrawal(200).yeild_interest().display_account_info()

