import util as u
from datetime import datetime
from dateutil import relativedelta
from dash import Dash, dcc, html
from financial_components import Investment
from financial_components import Income
from financial_components import Expense
import sqlite3

# TODO:
# 1. Have multiple dash subplots in new GUI file
# 2. Figure out what to display in each plot, what would be useful to know as a user? What would you want?
# 3. Generate dynamic frames for each plot (put plot in larger primary frame when selected)
# 4. Include page to insert data > passed to classes (need front end data input)
# 5. Implement database to save user info > create users, have data tied to each > design database tables

import plotly.express as px
import pandas as pd

class Budget():
    def __init__(self, name, allocated_amount):
        self.name = name
        self.allocated_amount = allocated_amount
        self.expenses = []
        self.incomes = []
        self.investments = []


    def save_to_database(self):
        """ Inserts expense object into the database """
        try:
            conn = sqlite3.connect("financials.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO budget (name, amount, category, frequency) VALUES (?, ?, ?, ?)
            ''', (self.name, self.amount, self.description, self.frequency))
            conn.commit()
            print("Success!")
        except sqlite3.Error as error:
            print("Failed to insert expense object into table: ", error)
        finally:
            cursor.close()

    def add_expense(self, name, amount, category, frequency):
        new_expense = Expense(name, amount, category, frequency)
        self.expenses.append(new_expense)


    def add_income(self, amount, category, frequency, date):
        new_income = Income(amount, category, frequency, date)
        self.incomes.append(new_income)


    def add_investment(self, amount, expected_return, frequency_of_return, category, maturity_date=None):
        new_investment = Investment(amount, expected_return, frequency_of_return, category, maturity_date)
        self.investments.append(new_investment)


    def calculate_total_annual_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.calculate_annual_amount()
        return total


    def calculate_total_annual_returns(self):
        total = 0
        for investment in self.investments:
            total += investment.calculate_annual_return()
        return total


    def calculate_net_annual_incomes(self):
        total_incomes = 0
        for income in self.incomes:
            total_incomes += income.amount
        total_expenses = self.calculate_total_annual_expenses()
        total_investments = self.calculate_total_annual_returns()
        return total_incomes - total_expenses + total_investments
    

    def generate_annual_expenses_data(self, start_date, end_date):
        dates = pd.date_range(start=start_date, end=end_date, freq='Y')
        annual_expenses = []
        for date in dates:
            annual_expense = sum(expense.calculate_annual_amount() for expense in self.expenses)
            annual_expenses.append(annual_expense)
        return dates, annual_expenses


    def generate_investments_accrual_data(self, start_date, end_date):
        dates = pd.date_range(start=start_date, end=end_date, freq='Y')
        investments_accrual = []
        for date in dates:
            annual_accrual = sum(investment.calculate_annual_return() for investment in self.investments)
            investments_accrual.append(annual_accrual)
        return dates, investments_accrual


    # ** PLOTTING BELOW **


    def plot_annual_expenses(self, start_date, end_date):
        dates, annual_expenses = self.generate_annual_expenses_data(start_date, end_date)
        fig = px.line(x=dates, y=annual_expenses, labels={'x': 'Year', 'y': 'Annual Expenses'})
        fig.show()


    def plot_investments_accrual(self, start_date, end_date):
        dates, investments_accrual = self.generate_investments_accrual_data(start_date, end_date)
        fig = px.line(x=dates, y=investments_accrual, labels={'x': 'Year', 'y': 'Investments Accrual'})
        fig.show()




# Create test budget
my_budget = Budget()

my_budget.add_income(1200, "salary", "biweekly", "04-21-2023")
my_budget.add_income(130, "sidehustle", "monthly", "08-01-2023")

my_budget.add_expense("rent", 1000, "housing", "monthly" )
my_budget.add_expense("gas", 200, "transportation", "monthly")
my_budget.add_expense("netflix", 20, "recreation", "monthly")
my_budget.add_expense("groceries", 200, "food", "biweekly")
my_budget.add_expense("resturaunts", 50, "food", "biweekly")

my_budget.add_investment(3000, 6, "annually", "stock")

print(my_budget.incomes[0].get_income_list_since_date())

#start_date = "2020-01-01"
#end_date = "2021-01-01"
#my_budget.plot_annual_expenses(start_date, end_date)