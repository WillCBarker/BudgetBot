import sqlite3
from sqlite3 import Error
from financial_components import Income

class IncomeDao:
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
                CREATE TABLE IF NOT EXISTS income (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    source TEXT NOT NULL,
                    amount REAL NOT NULL,
                    frequency TEXT NOT NULL,
                    date TEXT NOT NULL,
                    budget_id INTEGER NOT NULL,
                    FOREIGN KEY (budget_id) REFERENCES budget(id)
                )
            ''')
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            self.disconnect()

    def save_income(self, income):
        try:
            self.connect()
            self.cursor.execute('''
                INSERT INTO income (name, source, amount, frequency, date, budget_id) VALUES (?, ?, ?, ?, ?, ?)
            ''', (income.name, income.source, income.amount, income.frequency, income.date, income.budget_id))
            self.connection.commit()
        except Error as e:
            print(f"Error saving income: {e}")
        finally:
            self.disconnect()

    def get_income_by_name(self, income_name):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM income WHERE name = ?
            ''', (income_name,))
            income_data = self.cursor.fetchone()

            if income_data:
                income = Income(*income_data[1:])  # Skip the 'id' field
                return income
            else:
                return None
        except Error as e:
            print(f"Error getting income by name: {e}")
        finally:
            self.disconnect()

    def get_all_incomes(self):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM income
            ''')
            incomes_data = self.cursor.fetchall()

            incomes = []
            for income_data in incomes_data:
                income = Income(*income_data[1:])  # Skip the 'id' field
                incomes.append(income)

            return incomes
        except Error as e:
            print(f"Error getting all incomes: {e}")
        finally:
            self.disconnect()
