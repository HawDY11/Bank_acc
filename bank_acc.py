class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено на {amount}. Поточний баланс: {self.balance}.")
        else:
            print("Сума поповнення повинна бути більшою за нуль.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути більшою за нуль.")
        elif amount > self.balance:
            print("Недостатньо коштів для зняття.")
        else:
            self.balance -= amount
            print(f"Знято {amount}. Поточний баланс: {self.balance}.")

account = BankAccount("UA123456789", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
