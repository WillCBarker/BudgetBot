from datetime import datetime
from dateutil import relativedelta


def get_time_difference(start_date, end_date):
    """
    Get the time between to dates
    """

    time_difference = end_date - start_date

    return int(time_difference.days)


def get_occurences_in_time_interval(days, frequency):
    """
    Get the number of occurences in given amount of days based on given frequency
    """

    days_between_occurrence =  (365/frequency)
    occurences_in_time_interval = days//days_between_occurrence
    
    return int(occurences_in_time_interval)+1

def convert_frequency_of_return(frequency):
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

    return frequency_dict[frequency]

def compound_occurences_in_list(amount, occurences):
    occurence_list = []
    total = amount

    for i in range(occurences):
        occurence_list.append(total)
        total += amount
    
    return occurence_list