import os
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from datetime import datetime

# Constants
CSV_FILE = 'transactions.csv'
CATEGORIES = ['Income', 'Food', 'Rent', 'Utilities', 'Entertainment', 'Transport', 'Healthcare', 'Others']

# Initialize CSV if not exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount', 'Balance'])
    df.to_csv(CSV_FILE, index=False)

def load_data():
    return pd.read_csv(CSV_FILE)

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

def add_transaction():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format.")
            return
    description = input("Enter description: ")
    print("Select category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    try:
        category = CATEGORIES[int(input("Enter category number: ")) - 1]
    except (IndexError, ValueError):
        print("Invalid category.")
        return
    try:
        amount = float(input("Enter amount (use negative for expenses): "))
    except ValueError:
        print("Invalid amount.")
        return
    df = load_data()
    balance = df['Balance'].iloc[-1] + amount if not df.empty else amount
    new_transaction = {'Date': date, 'Description': description, 'Category': category, 'Amount': amount, 'Balance': balance}
    df = df.append(new_transaction, ignore_index=True)
    save_data(df)
    print("Transaction added successfully.")

def view_transactions():
    df = load_data()
    if df.empty:
        print("No transactions found.")
    else:
        print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

def generate_report():
    df = load_data()
    if df.empty:
        print("No transactions to generate report.")
        return
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    monthly = df.resample('M').sum()
    print("Monthly Report:")
    print(tabulate(monthly[['Amount', 'Balance']], headers='keys', tablefmt='pretty'))
    plt.figure(figsize=(10,5))
    plt.plot(monthly.index, monthly['Amount'], marker='o')
    plt.title('Monthly Income and Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.grid(True)
    plt.savefig('monthly_report.png')
    plt.show()
    df.reset_index(inplace=True)

def visualize_spending():
    df = load_data()
    if df.empty:
        print("No transactions to visualize.")
        return
    expenses = df[df['Amount'] < 0]
    if expenses.empty:
        print("No expenses to visualize.")
        return
    category_sum = expenses.groupby('Category')['Amount'].sum().abs()
    plt.figure(figsize=(8,8))
    category_sum.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.ylabel('')
    plt.savefig('spending_visualization.png')
    plt.show()

def main_menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Monthly Report")
        print("4. Visualize Spending")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            visualize_spending()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
