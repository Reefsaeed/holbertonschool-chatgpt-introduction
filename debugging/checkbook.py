#!/usr/bin/python3

class Checkbook:
    """A simple checkbook program to manage deposits, withdrawals, and balance checks."""

    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit a positive amount to the checkbook balance.

        Args:
            amount (float): The amount to deposit.

        Prints the deposited amount and updated balance.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw a positive amount if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw.

        Prints the withdrawn amount and updated balance, or an error if funds are insufficient.
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
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main loop to interact with the user for deposits, withdrawals, balance checks, and exit.

    Uses error handling to prevent crashes on invalid input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action in ['deposit', 'withdraw']:
            try:
                amount_str = input(f"Enter the amount to {action}: $")
                # إزالة أي علامة $ أو مسافات
                amount = float(amount_str.replace('$', '').strip())
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
