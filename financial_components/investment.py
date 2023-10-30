import util as u
import sqlite3

class Investment():
    def __init__(self, name, amount, roi, roi_frequency, description, maturity_date=None):
        """
        name: title/name of investment
        amount: investment amount, e.g. 3000
        roi: investment expected return percentage, e.g. 6 (percent)
        roi_frequency: how frequent returns are, e.g. annually
        description: description of investment
        maturity_date: date investment matures (for bonds), e.g. 10/12/2023
        """
        
        self.name = name
        self.amount = amount
        self.roi = roi
        self.roi_frequency = roi_frequency
        self.description = description
        self.maturity_date = maturity_date
    

    def save_to_database(self):
        """ Inserts investment object into the database """
        try:
            conn = sqlite3.connect("financials.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO investment (name, amount, roi, roi_frequency, description, maturity_date) VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.name, self.amount, self.roi, self.roi_frequency, self.description, self.maturity_date))
            conn.commit()
            print("Success!")
        except sqlite3.Error as error:
            print("Failed to insert investment object into table: ", error)
        finally:
            cursor.close()

    def convert_roi_frequency(self):
        """
        Returns the frequency of returns in a year based on "roi_frequency"
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

        return frequency_dict[self.roi_frequency]
        

    def convert_roi(self):
        """
        Converts roi to a number to be used in compounding income functions
        """

        return (self.roi/100) + 1
    

    def calculate_annual_return(self):
        """
        Gets annual return based on 
        """

        converted_roi = self.convert_roi()
        frequency = self.convert_roi_frequency()
        result = self.amount
        for i in range(frequency):
            result = result * converted_roi

        return result
    

    def calculate_accrued_return(self, start_date, end_date):
        """
        Return total amount accrued in the given time interval
        """

        converted_roi = self.convert_roi()
        days = u.get_time_difference(start_date, end_date)
        frequency = self.convert_roi_frequency()
        occurences_in_time_interval = u.get_occurences_in_time_interval(days, frequency)

        result = self.amount
        for i in range(occurences_in_time_interval):
            result = result * converted_roi

        return result