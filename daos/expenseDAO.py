import sqlite3
from sqlite3 import Error
from financial_components import Expense

class ExpenseDao:
    def __init__(self, db_path='financials.db'):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def create_table(self):
        try:
            self.connect()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS expense (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    frequency TEXT NOT NULL
                )
            ''')
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            self.disconnect()

    def save_expense(self, expense):
        try:
            self.connect()
            self.cursor.execute('''
                INSERT INTO expense (name, amount, category, frequency) VALUES (?, ?, ?, ?)
            ''', (expense.name, expense.amount, expense.category, expense.frequency))
            self.connection.commit()
        except Error as e:
            print(f"Error saving expense: {e}")
        finally:
            self.disconnect()

    def get_expense_by_name(self, expense_name):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM expense WHERE name = ?
            ''', (expense_name,))
            expense_data = self.cursor.fetchone()

            if expense_data:
                # Assuming the Expense class has a constructor that matches the database schema
                expense = Expense(*expense_data[1:])  # Skip the 'id' field
                return expense
            else:
                return None
        except Error as e:
            print(f"Error getting expense by name: {e}")
        finally:
            self.disconnect()

    def get_all_expenses(self):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM expense
            ''')
            expenses_data = self.cursor.fetchall()

            expenses = []
            for expense_data in expenses_data:
                # Assuming the Expense class has a constructor that matches the database schema
                expense = Expense(*expense_data[1:])  # Skip the 'id' field
                expenses.append(expense)

            return expenses
        except Error as e:
            print(f"Error getting all expenses: {e}")
        finally:
            self.disconnect()
