import util as u


class Cashflow():
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