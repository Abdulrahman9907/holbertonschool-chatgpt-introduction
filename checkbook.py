#!/usr/bin/python3

class Checkbook:
    """
    Function Description:
    A simple checkbook management system that allows users to deposit money,
    withdraw money, and check their current balance. The class maintains
    a running balance and provides formatted output for all transactions.
    
    Parameters:
    None for the class itself
    
    Returns:
    A Checkbook instance with methods for financial operations
    """
    
    def __init__(self):
        """
        Function Description:
        Initializes a new Checkbook instance with a starting balance of $0.00
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Adds the specified amount to the current balance and displays
        the transaction details and updated balance
        
        Parameters:
        amount (float): The amount of money to deposit (must be positive)
        
        Returns:
        None
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
            
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Subtracts the specified amount from the current balance if sufficient
        funds are available, otherwise displays an insufficient funds message
        
        Parameters:
        amount (float): The amount of money to withdraw (must be positive)
        
        Returns:
        None
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
            
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Displays the current account balance
        
        Parameters:
        None
        
        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def get_amount_input(prompt):
    """
    Function Description:
    Safely gets a monetary amount from user input with error handling
    for invalid inputs (non-numeric values, negative numbers)
    
    Parameters:
    prompt (str): The message to display when asking for input
    
    Returns:
    float: A valid positive monetary amount, or None if user wants to cancel
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() in ['cancel', 'exit', 'quit']:
                return None
            amount = float(user_input)
            if amount < 0:
                print("Amount cannot be negative. Please enter a positive number.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number (or 'cancel' to return to menu).")

def main():
    """
    Function Description:
    Main program loop that provides a command-line interface for the checkbook
    system. Handles user input and calls appropriate methods based on user choices.
    
    Parameters:
    None
    
    Returns:
    None
    """
    cb = Checkbook()
    print("Welcome to your Checkbook Management System!")
    print("Available commands: deposit, withdraw, balance, exit")
    
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip()
            
            if action.lower() == 'exit':
                print("Thank you for using the Checkbook Management System!")
                break
            elif action.lower() == 'deposit':
                amount = get_amount_input("Enter the amount to deposit: $")
                if amount is not None:
                    cb.deposit(amount)
            elif action.lower() == 'withdraw':
                amount = get_amount_input("Enter the amount to withdraw: $")
                if amount is not None:
                    cb.withdraw(amount)
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
                print("Available commands: deposit, withdraw, balance, exit")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
