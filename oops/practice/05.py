class BankAccount:
    def __init__(self,balance,owner_name):
        self.__balance = balance
        self.__owner_name = owner_name

    def deposit(self):
        deposit_amount = int(input("Enter the amount you want to deposit: "))
        self.__balance += deposit_amount
        return f"Rs.{deposit_amount} deposited successfully!"
    def withdraw(self):
        withdrawing_amount = int(input("Enter the amount you want to withdraw: "))
        if withdrawing_amount > self.__balance:
            return "Insufficient Balance"
        else:
            self.__balance -= withdrawing_amount
            return f"{withdrawing_amount} withdrawed successfully!"
    def balance(self):
        return f"Owner Name:{self.__owner_name} \nBalance: {self.__balance}"
account1 = BankAccount(2000,"Suprim Khatri")
print(account1.deposit())
print(account1.withdraw())
print(account1.balance())