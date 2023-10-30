import util as u
import sqlite3

class Expense():
    def __init__(self, name, amount, description, frequency):
        """
        name: expense name, e.g. Electricity
        amount: expense amount, e.g. 200
        description: description of expense
        frequency: frequency of expense charge, e.g. monthly
        """

        self.name = name
        self.amount = amount
        self.description = description
        self.frequency = frequency


    def save_to_database(self):
        """ Inserts expense object into the database """
        try:
            conn = sqlite3.connect("financials.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO expense (name, amount, description, frequency) VALUES (?, ?, ?, ?)
            ''', (self.name, self.amount, self.description, self.frequency))
            conn.commit()
            print("Success!")
        except sqlite3.Error as error:
            print("Failed to insert expense object into table: ", error)
        finally:
            cursor.close()

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
        frequency = u.convert_frequency_of_return(self.frequency)
        occurences_in_time_interval = u.get_occurences_in_time_interval(days, frequency)
        result = 0
        
        for i in range(occurences_in_time_interval):
            result += self.amount

        return result