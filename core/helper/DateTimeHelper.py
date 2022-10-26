from datetime import datetime
import pytz

"""
    File to handle date and time objects.
    This file provides static methods to work with date and time objects
"""

def formatDateTime(date,fmtIn,fmtOut,utc=False):
    """
        This method take a :date: with :fmtIn: format from UTC timezone
        and returns a string with :fmtOut: format and ARG timezone setted

        :raise ValueError: Invalid input date format

        :param date: str, e.g: "2020-07-29T16:11:15.803Z"
        :param fmtIn: str, e.g: "%Y-%m-%dT%H:%M:%S.%fZ"
        :param fmtOut: str, e.g: "%#d/%#m/%Y %H:%M"
        :param utc (optional): bool
        :return: str: e.g: "29/7/2020 13:11"
    """
    try:
        if (utc):
            tz = pytz.timezone(pytz.country_timezones['ar'][0])
            result = tz.fromutc(datetime.strptime(date, fmtIn))
        else:
            result = datetime.strptime(date, fmtIn)
    except ValueError:
        raise ValueError('Invalid input date format. [FormatInput: {}][DateInput: {}]'.format(date,fmtIn))
    return result.strftime(fmtOut)
