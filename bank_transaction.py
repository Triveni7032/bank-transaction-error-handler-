# Bank Transaction Error Handler
# Demonstrates Exception Handling in Python

balance = 10000
FILE_NAME = "transactions.txt"


def check_balance():
    print("\nCurrent Balance:", balance)


def deposit_money():
    global balance

    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        balance += amount

        with open(FILE_NAME, "a") as file:
            file.write("Deposited: " + str(amount) + "\n")

    except ValueError as error:
        print("Error:", error)

    else:
        print("Money deposited successfully.")
        print("Updated balance:", balance)

    finally:
        print("Deposit operation completed.")


def withdraw_money():
    global balance

    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > balance:
            raise Exception("Insufficient balance.")

        balance -= amount

        with open(FILE_NAME, "a") as file:
            file.write("Withdrawn: " + str(amount) + "\n")

    except ValueError as error:
        print("Invalid input:", error)

    except Exception as error:
        print("Transaction error:", error)

    else:
        print("Money withdrawn successfully.")
        print("Remaining balance:", balance)

    finally:
        print("Withdrawal operation completed.")


def view_transactions():
    try:
        with open(FILE_NAME, "r") as file:
            transactions = file.readlines()

        if len(transactions) == 0:
            print("No transactions found.")
        else:
            print("\n===== TRANSACTIONS =====")

            for transaction in transactions:
                print(transaction.strip())

    except FileNotFoundError:
        print("Transaction file does not exist.")

    finally:
        print("Transaction viewing operation completed.")


def main():

    while True:

        print("\n===== BANK TRANSACTION SYSTEM =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transactions")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit_money()

        elif choice == 3:
            withdraw_money()

        elif choice == 4:
            view_transactions()

        elif choice == 5:
            print("Thank you for using the Bank Transaction System.")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


main()