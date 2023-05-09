# Define initial balance
balance = 5000

# Define functions for different ATM operations
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Amount withdrawn:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("Current balance:", balance)

def check_balance():
    global balance
    print("Current balance:", balance)

# Main program loop
while True:
    print("\nWelcome to XYZ Bank ATM")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Quit")

    # Get user input
    choice = input("Enter your choice: ")

    # Execute user's choice
    if choice == "1":
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print("Thank you for using XYZ Bank ATM")
        break
    else:
        print("Invalid choice. Try again.")
