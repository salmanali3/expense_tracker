import csv
import os
import datetime

FILE_NAME = "expenses.csv"

def show_csv_path():
    print("\n📁 CSV File Location:")
    print(os.path.abspath(FILE_NAME))
    print("---------------------------------------")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, Other): ")
    amount = input("Enter amount: ")
    note = input("Enter note: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("Expense added successfully!")

def view_expenses():
    print("\n--- Expense History ---")
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found!")

def total_expense():
    total = 0
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
        print(f"\nTotal Expense: Rs {total}")
    except FileNotFoundError:
        print("No data available.")

def menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        show_csv_path()  # 
        print("1. Add Expense")
        print("2. View Expense History")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()
