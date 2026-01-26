class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner      
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance



account = BankAccount("Arsen", 2000)


account.deposit(400)
account.deposit(-50)     

account.withdraw(1000)
account.withdraw(2000)    

print("Final balance:", account.get_balance())
