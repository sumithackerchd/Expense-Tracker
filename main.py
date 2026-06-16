from database import (
    create_database,
    add_expense,
    view_expenses,
    delete_expense,
    search_expense
)


create_database()

while True:

    print("\n===== Expense Tracker =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

if choice == "1":

    title = input("Enter Expense Title: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD-MM-YYYY): ")

    add_expense(title, amount, date)

    print("Expense Added Successfully!")

elif choice == "2":

    expenses = view_expenses()

    print("\n===== Expense Records =====")

    for expense in expenses:
        print(expense)

elif choice == "3":

    expense_id = int(input("Enter Expense ID to delete: "))

    delete_expense(expense_id)

    print("Expense Deleted Successfully!")


elif choice == "4":

    title = input("Enter Expense Title: ")

    results = search_expense(title)

    print("\n===== Search Results =====")

    for expense in results:
        print(expense)    

else:

    print("Invalid Choice")