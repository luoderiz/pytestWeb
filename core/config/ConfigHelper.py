import json

class ConfigHelper:

    """
        Class to get parameters from the config.json file.
        This class implements a Singleton Pattern.
    """

    __instance = None
    __config = None
    __browser = None
    __driverPath = None
    __urlApp = None
    __defaultWait = None
    __incognito = False
    __headless = False
    __windowSize = None
    __extensions = None
    __lang = None
    __capabilities = None

    @staticmethod
    def getInstance():
        """
            Singleton Pattern to create an instance from ConfigHelper. 
            If the instance doesn't exist this method call to create it. Otherwise, It returns it.
            
            :return: ConfigHelper
        """
        if ConfigHelper.__instance == None:
            ConfigHelper().__loadParameters()
        return ConfigHelper.__instance

    def __init__(self):
        """
            Constructor to set the private variable __instance into self.
            If this constructor is called and __instance exists, It will raise a NotImplementedError

            :raise: NotImplementedError
        """
        if ConfigHelper.__instance != None:
            raise NotImplementedError("This is a Singlenton Class")
        ConfigHelper.__instance = self


    def __loadParameters(self):
        """
            Loads all parameters from the config.json file
        """
        with open('./config.json') as configFile:
            self.__config = json.load(configFile)
            self.__browser = self.__config['browser']
            self.__driverPath = self.__config['driverPath']
            self.__urlApp = self.__config['urlApp']
            self.__defaultWait = self.__config['defaultWait']
            self.__incognito = self.__config['incognito']
            self.__headless = self.__config['headless']['enabled']
            self.__windowSize = self.__config['headless']['window_size']
            self.__extensions = self.__config.get('extensions')
            self.__lang = self.__config.get('lang')
            self.__capabilities = self.__config.get('capabilities')

    def getUrlApp(self):
        """
            Return the current URL setted on the config.json file
            :return: string
        """
        return self.__urlApp
    
    def getBrowser(self):
        """
            Return the current Browser name setted on the config.json file
            :return: string
        """
        return self.__browser

    def getDriverPath(self):
        """
            Return the current Path setted on the config.json file for the webdriver
            :return: string
        """
        return self.__driverPath

    def getDefaultWait(self):
        """
            Return the current wait time setted on the config.json file for the Default Wait
            :return: int
        """
        return self.__defaultWait

    def getIncognitoMode(self):
        """
            Return the current Incognito mode setted on the config.json file
            :return: bool
        """
        return self.__incognito

    def getHeadlessMode(self):
        """
            Return the current Headless mode setted on the config.json file
            :return: bool
        """
        return self.__headless

    def getWindowSize(self):
        """
            Return the desired window size for headless mode. This not apply to headless=True
            :return: json 
        """
        return self.__windowSize
    
    def getExtensions(self):
        """
            Return a list with desired extensions for browser.
            :return: list
        """
        return self.__extensions

    def getLang(self):
        """
            Return a list with desired extensions for browser.
            :return: list
        """
        return self.__lang

    def getCapabilities(self):
        """
            Return a dict with desired capabilities for browser.
            :return: dict
        """
        return self.__capabilities