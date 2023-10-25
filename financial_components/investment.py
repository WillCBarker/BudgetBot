import util as u


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
        """
        Gets annual return based on 
        """

        converted_expected_return = self.convert_expected_return()
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