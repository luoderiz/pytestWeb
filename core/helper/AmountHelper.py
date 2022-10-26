"""
    File to handle amount objects.
    This file provides static methods to work with amount objects
"""

from decimal import Decimal
from unicodedata import decimal


def formatAmount(amount=''):
    try:
        if ('.00' in amount):
            return amount.replace('.00','')
        else:
            amount = str(Decimal(amount).normalize())
            return amount.replace('.',',')
            
    except ValueError:
        raise ValueError('Invalid input amount format. [AmountInput: {}]'.format(amount))
