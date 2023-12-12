import sqlite3
from sqlite3 import Error
from financial_components import Investment

class InvestmentDao:
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
                CREATE TABLE IF NOT EXISTS investment (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    amount REAL NOT NULL,
                    roi REAL NOT NULL,
                    roi_frequency TEXT NOT NULL,
                    description TEXT NOT NULL,
                    maturity_date TEXT,
                    budget_id INTEGER NOT NULL,
                    FOREIGN KEY (budget_id) REFERENCES budget(id)
                )
            ''')
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            self.disconnect()

    def save_investment(self, investment):
        try:
            self.connect()
            self.cursor.execute('''
                INSERT INTO investment (name, amount, roi, roi_frequency, description, maturity_date, budget_id) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (investment.name, investment.amount, investment.roi, investment.roi_frequency, investment.description, investment.maturity_date, investment.budget_id))
            self.connection.commit()
        except Error as e:
            print(f"Error saving investment: {e}")
        finally:
            self.disconnect()

    def get_investment_by_name(self, investment_name):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM investment WHERE name = ?
            ''', (investment_name,))
            investment_data = self.cursor.fetchone()

            if investment_data:
                investment = Investment(*investment_data[1:])  # Skip the 'id' field
                return investment
            else:
                return None
        except Error as e:
            print(f"Error getting investment by name: {e}")
        finally:
            self.disconnect()

    def get_all_investments(self):
        try:
            self.connect()
            self.cursor.execute('''
                SELECT * FROM investment
            ''')
            investments_data = self.cursor.fetchall()

            investments = []
            for investment_data in investments_data:
                investment = Investment(*investment_data[1:])  # Skip the 'id' field
                investments.append(investment)

            return investments
        except Error as e:
            print(f"Error getting all investments: {e}")
        finally:
            self.disconnect()
