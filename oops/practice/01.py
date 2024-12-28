class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self):
        depositAmount = float(input("Enter the amount to deposit: "))
        self.balance += depositAmount
        return f"Rs.{depositAmount} deposited successfully"
    def withdrawal(self):
        withdrawalAmount = float(input("Enter the amount you wan to withdraw: "))
        if withdrawalAmount <= self.balance:
            self.balance -= withdrawalAmount
            return f"Rs.{withdrawalAmount} withdrawn successfully!"
        else:
            return "Insufficient Balance!"
    def currBalance(self):
        return f"Current Balance is Rs.{self.balance}" 
my_balance = BankAccount(10000)
print(my_balance.currBalance())
print(my_balance.deposit())
print(my_balance.withdrawal())
print(my_balance.currBalance())
    
                              