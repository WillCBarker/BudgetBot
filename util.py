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
    
    return occurences_in_time_interval