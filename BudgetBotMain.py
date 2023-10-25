#tracks cashflow, budget, subscriptions, etc.
#shows projections on where money will be at in a period of time, A "what if" scenario
    #Describes where money will be at, what took the largest chunk between present date and set future date
#shows dashboard of all information

import util as u
from datetime import datetime
from dateutil import relativedelta
from dash import Dash, dcc, html

'''
Ideas:
    - "What if" scenarios, investing in certain stocks, predict yield over time using api pulled avg 20 yr gain for ex.
    - Initial questionaire using pyqt
'''


# class budget():
#     def __init__(self):
#         self.__housing = 0
#         self.__food = 0
#         self.__transportation = 0
#         self.__insurance = 0
#         self.__medical = 0
#         self.__utilities = 0
#         self.__investments = 0
#         self.__recreational = 0
#         self.__moneyIn = 0
#         self.__moneyOut = 0
#         self.__moneyIdle = 0
#         self.__expenseContainer = {'expenseNames': ['housing', 'food', 'transportation', 'insurance', 'medical', 'utilities', 'investments', 'recreational'],
#                                     'expenses' : [self.__housing, self.__food,  self.__transportation, 
#                                                     self.__insurance, self.__medical,  self.__utilities, 
#                                                     self.__investments, self.__recreational]}

#     def setMoneyIn(self, newMoneyIn):
#         self.__moneyIn = newMoneyIn
    
#     def setMoneyOut(self, newMoneyOut):
#         self.__moneyOut = newMoneyOut

#     def setMoneyIdle(self, newMoneyIdle):
#         self.__moneyIdle = newMoneyIdle

#     def setHousing(self, newHousing):
#         self.__housing = newHousing
#         self.__expenseContainer['expenses'][0] = self.__housing

#     def setFood(self, newFood):
#         self.__food = newFood
#         self.__expenseContainer['expenses'][1] = self.__food

#     def setTransportation(self, newTransportation):
#         self.__transportation = newTransportation
#         self.__expenseContainer['expenses'][2] = self.__transportation

#     def setInsurance(self, newInsurance):
#         self.__insurance = newInsurance
#         self.__expenseContainer['expenses'][3] = self.__insurance

#     def setMedical(self, newMedical):
#         self.__medical = newMedical
#         self.__expenseContainer['expenses'][4] = self.__medical

#     def setUtilities(self, newUtilities):
#         self.__utilities = newUtilities
#         self.__expenseContainer['expenses'][5] = self.__utilities

#     def setInvestments(self, newInvestments):
#         self.__investments = newInvestments
#         self.__expenseContainer['expenses'][6] = self.__investments

#     def setRecreational(self, newRecreational):
#         self.__recreational = newRecreational
#         self.__expenseContainer['expenses'][7] = self.__recreational

#     def getMoneyIn(self):
#         return self.__moneyIn

#     def getMoneyOut(self):
#         return self.__moneyOut

#     def getMoneyIdle(self):
#         return self.__moneyIdle

#     def getExpenseContainer(self):
#         return self.__expenseContainer

#     '''
#     Methods directly associated with plotting below
#     '''

#     def getCostliestCategory(self):
#         '''
#         Returns most costly category of budget
#         @return int
#         '''
#         maxIndex = self.__expenseContainer['expenses'].index(max(self.__expenseContainer['expenses']))
#         return self.__expenseContainer['expenseNames'][maxIndex]


#     def getTotalBudget(self):
#         '''
#         Returns sum of all categories in budget
#         @return int
#         '''
#         return sum(self.__expenseContainer['expenses'])

#     def getDiscretionaryIncome(self):
#         '''
#         Returns money available after all expenses paid
#         @return int
#         '''
#         return self.netIncome() - self.getTotalBudget()

#     def getTax(self):
#         '''
#         Calculates state and federal income tax rate given income.
#         Notes:
#             -State tax based on Virginia only 
#             -Federal tax based assumes single filing
#         @return int
#         '''
#         #State Tax brackets
#         if self.__moneyIn <= 3000: stateTax = 0.98
#         elif self.__moneyIn <= 50000: stateTax = 0.97
#         elif self.__moneyIn <= 17000: stateTax = 0.95
#         else: stateTax = 0.9425

#         #Federal Tax brackets
#         if self.__moneyIn <= 10275: federalTax = 0.10 * self.__moneyIn
#         elif self.__moneyIn <= 10276: federalTax = 1027.50 + (0.12 * (self.__moneyIn - 10275))
#         elif self.__moneyIn <= 41776: federalTax = 4807.50 + (0.22 * (self.__moneyIn - 41775))
#         elif self.__moneyIn <= 89076: federalTax = 15213.50 + (0.24 * (self.__moneyIn - 89075))
#         elif self.__moneyIn <= 170051: federalTax = 34647.50 + (0.32 * (self.__moneyIn - 170050))
#         elif self.__moneyIn <= 215951: federalTax = 49335.50 + (0.35 * (self.__moneyIn - 215950))
#         else: federalTax = 162718 + (0.37 * (self.__moneyIn - 539900))

#         return stateTax, federalTax

#     def netIncome(self):
#         '''
#         Calculates income after tax
#         @return int
#         '''
#         stateTax, federalTax = self.getTax()
#         return (self.__moneyIn * stateTax) - federalTax

#     def projectMoney(self, date):
#         '''
#         Shows where money will be at input future date based on budget, returning 2 lists - 1. monthly/yearly balance, 2. month/year count
#         @return list
#         '''
#         timeDiff = self.monthDifference(date)
#         if timeDiff > 12:
#             #if date is over 1 year in the future, plot by year instead of month
#             timeDiff = round(timeDiff/12) + 1
#             start = 1
#         else:
#             #A year and under, plots the single year since data is incremented by year
#             timeDiff = 2
#             start = 0

#         balance = []
#         count = []
#         for i in range(start, timeDiff):
#             balance.append(i*self.getDiscretionaryIncome())
#             count.append(i)
#         return [count, balance]


#     def monthDifference(self, date):
#         '''
#         Uses datetime & relativedelta to find difference between 2 dates in months
#         @return int
#         '''
#         today = datetime.now().strftime('%Y-%m-%d')
#         date = date.strftime('%Y-%m-%d')
#         start_date = datetime.strptime(today, "%Y-%m-%d")
#         end_date = datetime.strptime(date, "%Y-%m-%d")
#         diff = relativedelta.relativedelta(end_date, start_date)
#         return diff.months + (diff.years * 12)

#     def compoundInterest(self, end_date, percentGrowth):
#         '''
#         Calculates compound interest based on input time frame and yield
#         @return list
#         '''
#         profit = self.__investments
#         percentGrowth = percentGrowth/100
#         yearDiff = self.monthDifference(end_date)//12
#         profitTrack = []
#         yearCount = []
#         for i in range(yearDiff):
#             profit = profit * (1 + percentGrowth) + self.__investments
#             profitTrack.append(profit)
#             yearCount.append(i)
#         return [yearCount, profitTrack]

# ''' --Test Code
# x = budget()
# x.setFood(500)
# x.setInsurance(300)
# x.setMoneyIn(95000)
# print("Costliest: ", x.getCostliestCategory())
# print("total Budget: ", x.getTotalBudget())
# print("Disc Income: ", x.getDiscretionaryIncome())
# futureDay = datetime(2024, 8, 30) #going to need time setting method for GUI
# x.projectMoney(futureDay)
# '''

# *************************************************************************************************************

# TODO:
# 1. Have multiple dash subplots in new GUI file
# 2. Figure out what to display in each plot, what would be useful to know as a user? What would you want?
# 3. Generate dynamic frames for each plot (put plot in larger primary frame when selected)
# 4. Include page to insert data > passed to classes (need front end data input)
# 5. Implement database to save user info > create users, have data tied to each > design database tables

import plotly.express as px
import pandas as pd

class Budget():
    def __init__(self):
        self.expenses = []
        self.cashflows = []
        self.investments = []


    def add_expense(self, name, amount, category, frequency):
        new_expense = Expense(name, amount, category, frequency)
        self.expenses.append(new_expense)


    def add_cashflow(self, amount, category, frequency, date):
        new_cashflow = CashFlow(amount, category, frequency, date)
        self.cashflows.append(new_cashflow)


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


    def calculate_net_annual_cashflows(self):
        total_cashflows = 0
        for cashflow in self.cashflows:
            total_cashflows += cashflow.amount
        total_expenses = self.calculate_total_annual_expenses()
        total_investments = self.calculate_total_annual_returns()
        return total_cashflows - total_expenses + total_investments
    

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


    def plot_annual_expenses(self, start_date, end_date):
        dates, annual_expenses = self.generate_annual_expenses_data(start_date, end_date)
        fig = px.line(x=dates, y=annual_expenses, labels={'x': 'Year', 'y': 'Annual Expenses'})
        fig.show()


    def plot_investments_accrual(self, start_date, end_date):
        dates, investments_accrual = self.generate_investments_accrual_data(start_date, end_date)
        fig = px.line(x=dates, y=investments_accrual, labels={'x': 'Year', 'y': 'Investments Accrual'})
        fig.show()


class Expense():
    def __init__(self, name, amount, category, frequency):
        """
        name: expense name, e.g. Electricity
        amount: expense amount, e.g. 200
        category: expense category, e.g. utilities
        frequency: frequency of expense charge, e.g. monthly
        """
        self.name = name
        self.amount = amount
        self.category = category
        self.frequency = frequency


    def calculate_annual_amount(self):
        # TO BE REPLACED BY UTIL (shared with convert frequency of return)
        frequency_dict = {
            "daily": 365,
            "weekly": 52,
            "biweekly": 26,
            "monthly": 12,
            "quarterly": 4,
            "semiannual": 2,
            "annually": 1
        }

        return self.amount * frequency_dict[self.frequency]
        
    def calculate_accrued_expense(self, start_date, end_date):
        days = u.get_time_difference(start_date, end_date)
        frequency = self.convert_frequency_of_return()
        occurences_in_time_interval = u.get_occurences_in_time_interval(days, frequency)

        for i in range(occurences_in_time_interval):
            result += self.amount

        return result


class CashFlow():
    def __init__(self, amount, category, frequency,  date):
        """
        amount: cashflow amount, e.g. 900
        category: cashflow category, e.g. Salary
        frequency: cashflow frequency, e.g. biweekly
        date: date of cashflow, e.g. 10/12/2023
        """
        self.amount = amount
        self.category = category
        self.frequency = frequency
        self.date = date


class Investment():
    def __init__(self, amount, expected_return, frequency_of_return, category, maturity_date=None):
        """
        amount: investment amount, e.g. 3000
        expected_return: investment expected return percentage, e.g. 6 (percent)
        category: investment category, e.g. Bond
        frequency_of_return: how frequent returns are, e.g. annually
        maturity_date: date investment matures (for bonds), e.g. 10/12/2023
        """
        self.amount = amount
        self.expected_return = expected_return
        self.frequency_of_return = frequency_of_return
        self.category = category
        self.maturity_date = maturity_date
    

    def convert_frequency_of_return(self):
        """
        Returns the frequency of returns in a year based on "frequency_of_return"
        """
        # NOTE: REPLACE THIS
        # With a util.py type method for every function to use for conversions (looking at you expenses)

        frequency_dict = {
            "daily": 365,
            "weekly": 52,
            "biweekly": 26,
            "monthly": 12,
            "quarterly": 4,
            "semiannual": 2,
            "annual": 1
        }

        return frequency_dict[self.frequency_of_return]
        

    def convert_expected_return(self):
        """
        Converts expected return to a number to be used in compounding income functions
        """

        return (self.expected_return/100) + 1
    

    def calculate_annual_return(self):
        converted_expected_return = converted_expected_return()
        frequency = self.convert_frequency_of_return()
        result = self.amount
        for i in range(frequency):
            result = result * converted_expected_return

        return result
    

    def calculate_accrued_return(self, start_date, end_date):
        """
        Return total amount accrued in the given time interval
        """

        converted_expected_return = converted_expected_return()
        days = u.get_time_difference(start_date, end_date)
        frequency = self.convert_frequency_of_return()
        occurences_in_time_interval = u.get_occurences_in_time_interval(days, frequency)

        result = self.amount
        for i in range(occurences_in_time_interval):
            result = result * converted_expected_return

        return result
    


my_budget = Budget()
# Add expenses and investments

start_date = "2020-01-01"
end_date = "2025-01-01"

my_budget.plot_annual_expenses(start_date, end_date)
my_budget.plot_investments_accrual(start_date, end_date)