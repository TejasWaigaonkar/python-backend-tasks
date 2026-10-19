
import json

# Load expenses
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save expenses
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount")


# View expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found")
    else:
        for expense in expenses:
            print(expense)


# Total expenses
def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses:", total)


# Delete expense
def delete_expense():
    view_expenses()

    try:
        number = int(input("Enter expense number to delete (starting from 1): "))

        if number >= 1 and number <= len(expenses):
            expenses.pop(number - 1)
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number")

    except ValueError:
        print("Please enter a valid number")


# Main program
expenses = load_expenses()

while True:
    print("EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
