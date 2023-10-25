import util as u


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
        """
        Calculates annual amount based on set frequency
        """
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
        """
        Calculates accrued expenses in a given time interval
        """
        
        days = u.get_time_difference(start_date, end_date)
        frequency = self.convert_frequency_of_return()
        occurences_in_time_interval = u.get_occurences_in_time_interval(days, frequency)

        for i in range(occurences_in_time_interval):
            result += self.amount

        return result