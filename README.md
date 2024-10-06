
# Daily Expenses Tracker in Python

A simple and efficient personal finance tracker built in Python using CSV to store and manage data. This application allows users to track income, expenses, and generate financial reports. It provides clear insights into personal financial activities with data visualizations.

## Features

- **Add Transactions**: Record income or expense transactions with a category, description, and amount.
- **View Transactions**: See all your transactions in a table format.
- **Generate Monthly Report**: Summarize your financial activities on a monthly basis.
- **Visualize Spending**: View a pie chart breakdown of expenses by category to track where your money is going.
- **Balance Tracking**: Automatically updates your running balance after every transaction.

## How to Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yasinULLAH/daily-expenses-tracker-in-python
    cd daily-expenses-tracker-in-python
    ```

2. **Install Dependencies**:

    Make sure you have all the required libraries installed. You can install the necessary libraries using:

    ```bash
    pip install pandas matplotlib tabulate
    ```

3. **Run the Application**:

    To start tracking your daily expenses, run the following command:

    ```bash
    python personal_finance_tracker.py
    ```

4. **Features Available**:

   - **Add Transaction**: Input the details of your income or expenses.
   - **View Transactions**: Display all transactions recorded so far.
   - **Generate Monthly Report**: See the total income, expenses, and balance for each month.
   - **Visualize Spending**: View a pie chart of expenses categorized to help understand your spending habits.

## Data Management

- **CSV Database**: All data (transactions, categories, balances) are stored in a CSV file named `transactions.csv`. This file will be automatically created in the project directory if it doesn't exist.
- **Export/Import**: You can easily share or backup the CSV file or transfer it between systems for continuity.

## Project Structure

- `personal_finance_tracker.py`: Main script containing all the functionality.
- `transactions.csv`: The file where all transactions are stored.
- `monthly_report.png`: Monthly income/expenses graph.
- `spending_visualization.png`: Pie chart of expenses by category.

## Contributing

Contributions are welcome! Feel free to fork this repository, open an issue, or submit a pull request if you have suggestions for improvements or new features.

## License

This project is open-source and available under the [MIT License].
