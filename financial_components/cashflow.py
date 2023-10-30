import util as u
from datetime import date, datetime

class Cashflow():
    def __init__(self, amount, category, frequency,  date):
        """
        amount: cashflow amount, e.g. 900
        category: cashflow category, e.g. Salary
        frequency: cashflow frequency, e.g. biweekly
        date: date of cashflow, e.g. 10-12-2023
        """
        
        self.amount = amount
        self.category = category
        self.frequency = frequency
        self.date = datetime.strptime(date, '%m-%d-%Y').date()

    def get_cashflow_list_since_date(self):
        days = (date.today() - self.date).days
        return days