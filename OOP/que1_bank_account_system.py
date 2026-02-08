# Question 1: Bank Account System
# Write a program that simulates a basic bank account system with the following requirements:

# Requirements:
# The program should start with an initial balance of 10,000.
# Repeatedly display a menu to the user with the following options:
# Deposit
# Withdraw
# Check Balance
# Exit

# Based on the user’s choice:
# Deposit: Ask for an amount and add it to the balance.
# Withdraw: Ask for an amount and subtract it from the balance (ensure sufficient balance).
# Check Balance: Display the current balance.
# Exit: Terminate the program gracefully.
# The program should continue running until the user chooses the Exit option.

# Instructions:
# Implement proper input validation where necessary.
# Keep the program user-friendly with clear messages.

class BankAccount:
    '''
    Represents a simple bank account
    
    This class simulates functionalities of simple bank account like, depositing,
    withdrawing and check balance
    
    Attributes:
        balance (float): account balance
    '''
    
    def __init__(self, balance = 10000):
        '''
        Initialize bank account object
        
        Args:
            balance (float): balance in account (initially 10000)
        '''
        self.__balance = balance
        
    def check_balance(self) -> str:
        '''
        Checks balance of account
        
        Returns:
            str: current balance
        '''
        return self.__balance
    
    def deposit(self, amount: float) -> str:
        '''
        Deposits amount in bank account
        
        Args:
            amount (float): Amount to deposit in account
        Returns:
            str: success message
        '''
        if amount <= 0:
            return "Invalid Amount, amount should be more than 0."
        
        self.__balance += amount
        
        return "Deposit Successful."
    
    def witdraw(self, amount: float) -> str:
        '''
        Withdraws amount from bank account
        
        Args:
            amount (float): amount to withdraw
        Returns:
            str: success message
        '''        
        if amount > self.__balance:
            return "Insufficient Balance."
        
        self.__balance = round(self.__balance - amount,2)
        
        return "Withdraw Successful."
    
    @staticmethod
    def amount_input(operation: str) -> float:
        '''
        validates and takes input from user
        
        Args:
            operation (str): name of the operation
        Returns:
            float: amount as output
        '''
        while True:
            try: 
                amount = float(input(f"Enter {operation} amount: "))
                if amount <= 0:
                    print("Invalid Amount, amount should be more than 0.")
                    continue
                return amount
            except ValueError as e:
                print("Invalid amount, Enter again.")

def main():
    account = BankAccount()
    while True:
        print("Enter number between 1 and 4 to perform following operations: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        print("===================================")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError as e:
            print("Choice is invalid. Enter choice from 1 to 4.")
            print("===================================")
            continue
        
        match choice:
            case 1:
                amount = BankAccount.amount_input("Deposit")
                ans = account.deposit(amount)
                print(ans)
                print("===================================")
            case 2:
                amount = BankAccount.amount_input("Withdraw")
                ans = account.witdraw(amount)
                print(ans)
                print("===================================")
            case 3:
                ans = account.check_balance()
                print(ans)
                print("===================================")
            case 4:
                break
            case _:
                print("Input choice is invalid, Enter choice from 1 to 4.")
            
if __name__ == "__main__":
    main()