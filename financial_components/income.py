import util as u
from datetime import date, datetime
import sqlite3

class Income():
    def __init__(self, name, source, amount, frequency,  date):
        """
        name: name of the income object
        source: source of the income
        amount: Income amount, e.g. 900
        frequency: Income frequency, e.g. biweekly
        date: date of Income, e.g. 10-12-2023
        """
        
        self.name = name
        self.source = source
        self.amount = amount
        self.frequency = frequency
        self.date = datetime.strptime(date, '%m-%d-%Y').date()


    def save_to_database(self):
        """ Inserts income object into the database """
        try:
            conn = sqlite3.connect("financials.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO income (name, source, amount, frequency, date) VALUES (?, ?, ?, ?, ")
            ''', (self.name, self.source, self.amount, self.frequency, self.date))
            conn.commit()
            print("Success!")
        except sqlite3.Error as error:
            print("Failed to insert income object into table: ", error)
        finally:
            cursor.close()


    def get_income_list_since_date(self):
        days = (date.today() - self.date).days
        return days