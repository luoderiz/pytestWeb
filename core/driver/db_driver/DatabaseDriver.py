import pyodbc
from core.config.ConfigDBHelper import ConfigDBHelper


class DatabaseDriver():

    """
        Class to handle Database driver. This class not requiered an instance.
        To 'create' a instance, call the method 'getInstance()' that return a Singlenton DatabaseDriver
        for all steps requiered.
    """

    __instance = None
    __config = ConfigDBHelper.getInstance()

    def __init__(self):
        """
            This method doesn't be used! To create/get an instance of DatabaseDriver use 'getInstance()'
            :raise RuntimeError()
        """
        raise RuntimeError('Use getInstance() instead')

    @classmethod
    def getInstance(cls):
        """
            Singleton pattern to create an instance of DatabaseDriver in case that doesn't exist. 
            If exist an instance, return the same.
            :return: DatabaseDriver
        """
        if cls.__instance is None:
            cls.__instance = cls.__createDriver(cls)
        return cls.__instance

    def __createDriver(self):
        """
            This method creates an instance of DatabaseDriver.
            This DatabaseDriver is created with the settings that contain the file 'dbconfig.json'
            :param: DatabaseDriver
        """
        return pyodbc.connect("DRIVER={};SERVER={};DATABASE={};UID={};PWD={}".format(self.__config.getDBDriver(), 
            self.__config.getDBHost(), self.__config.getDBName(), self.__config.getDBUser(), self.__config.getDBPass()))

    @classmethod
    def closeDriver(cls):
        """
            A method that close driver and set the instance at None.
        """
        cls.__instance.close()
        cls.__instance=None