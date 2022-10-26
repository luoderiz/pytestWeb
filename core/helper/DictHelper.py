"""
    File to handle dictionaries.
    This file provides static methods to handle python dictionaries.
"""

def removeKeyData(dict, key):
    """
        Method to filter :key: entry from a dictionary.

        :param dict: dict
        :param key: str
        :return: dict
    """
    return {k: v for k, v in dict.items() if k != key}

def hideKeyData(dict, key):
    """
        method to replace the value of the :key: input with its classname.

        :param dict: dict
        :param key: str
    """
    if type(dict) == type({}):
        for k, v in dict.items():
            if (k == key):
                dict.update({k:type(v).__name__})
            else:
                dict.update({k:v})
            hideKeyData(v,key)
