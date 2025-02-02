class BankAccount:
    def __init__(self,name,AC_no,balance):
        self.name = name
        self.AC_no = AC_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Balance: {self.balance}"
def interface(BankAccount):
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            BankAccount.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            BankAccount.withdraw(amount)
        elif choice == 3:
            print(BankAccount.get_balance())
        elif choice == 4:
            exit()
            break
        else:
            print("Invalid choice")
    
    
    
    
def main():
    name = input("Enter the name of the account holder: ")
    AC_no = input("Enter the account number: ")
    balance = float(input("Enter the initial balance: "))
    account = BankAccount(name,AC_no,balance)
    interface(account)
main()
    