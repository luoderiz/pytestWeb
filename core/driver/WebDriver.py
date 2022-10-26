from core.config.ConfigHelper import ConfigHelper
from core.driver.FactoryDriver import FactoryDriver


class WebDriver(object):

    """
        Class to handle Selenium driver. This class not requiered an instance.
        To 'create' a instance, call the method 'getInstance()' that return a Singlenton WebDriver
        for all steps requiered.
    """

    __instance = None

    def __init__(self):
        """
            This method doesn't be used! To create/get an instance of WebDriver use 'getInstance()'
            :raise RuntimeError()
        """
        raise RuntimeError('Use getInstance() instead')

    @classmethod
    def getInstance(cls):
        """
            Singleton pattern to create an instance of WebDriver in case that doesn't exist. 
            If exist an instance, return the same.
            :return: WebDriver
        """
        if cls.__instance is None:
            cls.__instance = FactoryDriver().createDriver()
        return cls.__instance

    @classmethod
    def closeDriver(cls):
        """
            A method that close driver and set the instance at None.
        """
        cls.__instance.delete_all_cookies()
        cls.__instance.close()
        cls.__instance=None
