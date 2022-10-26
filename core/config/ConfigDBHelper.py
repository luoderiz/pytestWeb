import json, os

class ConfigDBHelper:

    """
        Class to get parameters from the dbconfig.json file.
        This class implements a Singleton Pattern.
    """

    __file = "./dbconfig.json"
    __instance = None
    __config = None
    __db_user = None
    __db_password = None
    __db_host = None
    __db_name = None
    __db_driver = None
    
    @staticmethod
    def getInstance():
        """
            Singleton Pattern to create an instance from ConfigDBHelper. 
            If the instance doesn't exist this method call to create it. Otherwise, It returns it.
            
            :return: ConfigDBHelper
        """
        if ConfigDBHelper.__instance == None:
            ConfigDBHelper().__loadParameters()
        return ConfigDBHelper.__instance

    def __init__(self):
        """
            Constructor to set the private variable __instance into self.
            If this constructor is called and __instance exists, It will raise a NotImplementedError

            :raise: NotImplementedError
        """
        if ConfigDBHelper.__instance != None:
            raise NotImplementedError("This is a Singlenton Class")
        ConfigDBHelper.__instance = self


    def __loadParameters(self):
        """
            Loads all parameters from the dbconfig.json file
        """
        if os.path.exists(self.__file):
            with open(self.__file) as configFile:
                self.__config = json.load(configFile)
                self.__db_user = self.__config['DB_USER']
                self.__db_password = self.__config['DB_PASS']
                self.__db_host = self.__config['DB_HOST']
                self.__db_name = self.__config['DB_DB']
                self.__db_driver = self.__config['DB_DRIVER']
        else:
            raise FileNotFoundError("Unable to find the file {}".format(self.__file))

    def getDBUser(self):
        """
            Return the current db username setted on the dbconfig.json file
            :return: str
        """
        return self.__db_user
    
    def getDBPass(self):
        """
            Return the current db password setted on the dbconfig.json file
            :return: str
        """
        return self.__db_password

    def getDBHost(self):
        """
            Return the current db host setted on the dconfig.json file
            :return: str
        """
        return self.__db_host

    def getDBName(self):
        """
            Return the current db name setted on the dbconfig.json file
            :return: str
        """
        return self.__db_name

    def getDBDriver(self):
        """
            Return the current db driver setted on the dbconfig.json file
            :return: str
        """
        return self.__db_driver