class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print('Deposit:',amount, ', Balance:', self.__balance)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print('Withdraw: ', amount, ', Balance:', self.__balance)
        else:
            print('Withdraw: ', amount, ', Not enough balance.')
