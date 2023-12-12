import sqlite3
from sqlite3 import Error

import budget as Budget
from financial_components import Income, Expense, Investment


class BudgetDao:
    def __init__(self, db_path="financials.db"):
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
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS budget (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    allocated_amount REAL NOT NULL
                )
            """)
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            self.disconnect()

    def save_budget(self, budget):
        try:
            self.connect()
            self.cursor.execute("""
                INSERT INTO budget (name, allocated_amount) VALUES (?, ?)
            """, (budget.name, budget.allocated_amount))
            self.connection.commit()
        except Error as e:
            print(f"Error saving budget: {e}")
        finally:
            self.disconnect()

    def save_complete_budget(self, budget):
        try:
            self.connect()

            # Save the budget
            self.cursor.execute('''
                INSERT INTO budget (name, allocated_amount) VALUES (?, ?)
            ''', (budget.name, budget.allocated_amount))
            self.connection.commit()

            # Get the ID of the saved budget
            budget_id = self.cursor.lastrowid

            # Save expenses
            for expense in budget.expenses:
                self.cursor.execute('''
                    INSERT INTO expense (name, amount, category, frequency, budget_id) VALUES (?, ?, ?, ?, ?)
                ''', (expense.name, expense.amount, expense.category, expense.frequency, budget_id))
            self.connection.commit()

            # Save incomes
            for income in budget.incomes:
                self.cursor.execute('''
                    INSERT INTO income (name, source, amount, frequency, date, budget_id) VALUES (?, ?, ?, ?, ?, ?)
                ''', (income.name, income.source, income.amount, income.frequency, income.date, budget_id))
            self.connection.commit()

            # Save investments
            for investment in budget.investments:
                self.cursor.execute('''
                    INSERT INTO investment (name, amount, roi, roi_frequency, description, maturity_date, budget_id) VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (investment.name, investment.amount, investment.roi, investment.roi_frequency, investment.description, investment.maturity_date, budget_id))
            self.connection.commit()

            print("Success! Budget and associated elements saved to the database.")
        except Error as e:
            print(f"Error saving complete budget: {e}")
        finally:
            self.disconnect()

    def get_budget_by_name(self, budget_name):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM budget WHERE name = ?
            """, (budget_name,))
            budget_data = self.cursor.fetchone()

            if budget_data:
                # Assuming the Budget class has a constructor that matches the database schema
                budget = Budget(*budget_data[1:])  # Skip the "id" field
                return budget
            else:
                return None
        except Error as e:
            print(f"Error getting budget by name: {e}")
        finally:
            self.disconnect()

    def get_all_budgets(self):
        try:
            self.connect()
            self.cursor.execute("""
                SELECT * FROM budget
            """)
            budgets_data = self.cursor.fetchall()

            budgets = []
            for budget_data in budgets_data:
                # Assuming the Budget class has a constructor that matches the database schema
                budget = Budget(*budget_data[1:])  # Skip the "id" field
                budgets.append(budget)

            return budgets
        except Error as e:
            print(f"Error getting all budgets: {e}")
        finally:
            self.disconnect()

    def get_expenses_for_budget(self, budget_name):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT id FROM budget WHERE name = ?
            ''', (budget_name,))
            budget_id = self.cursor.fetchone()

            if budget_id:
                budget_id = budget_id[0]  # Extract the budget_id from the tuple
                self.cursor.execute('''
                    SELECT * FROM expense WHERE budget_id = ?
                ''', (budget_id,))
                expenses_data = self.cursor.fetchall()

                expenses = []
                for expense_data in expenses_data:
                    expense = Expense(*expense_data[1:])  # Skip the 'id' field
                    expenses.append(expense)

                return expenses
            else:
                return None
        except Error as e:
            print(f"Error getting expenses for budget: {e}")
        finally:
            self.disconnect()

    def get_incomes_for_budget(self, budget_name):
        try:
            self.connect()
            # Assuming the budget table has a unique constraint on the name column
            self.cursor.execute('''
                SELECT id FROM budget WHERE name = ?
            ''', (budget_name,))
            budget_id = self.cursor.fetchone()

            if budget_id:
                budget_id = budget_id[0]  # Extract the budget_id from the tuple
                self.cursor.execute('''
                    SELECT * FROM income WHERE budget_id = ?
                ''', (budget_id,))
                incomes_data = self.cursor.fetchall()

                incomes = []
                for income_data in incomes_data:
                    # Assuming the Income class has a constructor that matches the database schema
                    income = Income(*income_data[1:])  # Skip the 'id' field
                    incomes.append(income)

                return incomes
            else:
                return None
        except Error as e:
            print(f"Error getting incomes for budget: {e}")
        finally:
            self.disconnect()

    def get_investments_for_budget(self, budget_name):
        try:
            self.connect()
            # Assuming the budget table has a unique constraint on the name column
            self.cursor.execute('''
                SELECT id FROM budget WHERE name = ?
            ''', (budget_name,))
            budget_id = self.cursor.fetchone()

            if budget_id:
                budget_id = budget_id[0]  # Extract the budget_id from the tuple
                self.cursor.execute('''
                    SELECT * FROM investment WHERE budget_id = ?
                ''', (budget_id,))
                investments_data = self.cursor.fetchall()

                investments = []
                for investment_data in investments_data:
                    # Assuming the Investment class has a constructor that matches the database schema
                    investment = Investment(*investment_data[1:])  # Skip the 'id' field
                    investments.append(investment)

                return investments
            else:
                return None
        except Error as e:
            print(f"Error getting investments for budget: {e}")
        finally:
            self.disconnect()


