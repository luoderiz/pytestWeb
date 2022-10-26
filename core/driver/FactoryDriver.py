from core.config.ConfigHelper import ConfigHelper
from selenium import webdriver

class FactoryDriver():

    __driver = None
    __config = ConfigHelper.getInstance()

    def createDriver(self):
        """
            This method creates an instance of WebDriver.
            This Webdriver is created with the settings that contain the file 'config.json'
            :param: WebDriver
        """
        if(self.__config.getBrowser() == "firefox"):
            firefoxProfile = webdriver.FirefoxProfile()
            firefoxOptions = webdriver.FirefoxOptions()
            firefoxProfile.set_preference('browser.privatebrowsing.autostart',self.__config.getIncognitoMode())
            firefoxProfile.set_preference("intl.accept_languages", "en")
            firefoxOptions.headless = self.__config.getHeadlessMode()
            if (self.__config.getCapabilities()):
                for k, v in self.__config.getCapabilities().items():
                    firefoxOptions.set_capability(k, v)                    
            self.__driver = webdriver.Firefox(timeout=self.__config.getDefaultWait(),
                executable_path=self.__config.getDriverPath(), firefox_profile=firefoxProfile,
                options=firefoxOptions)
        elif(self.__config.getBrowser() == "chrome"):
            chromeoptions = webdriver.ChromeOptions()
            if(self.__config.getIncognitoMode()):
                chromeoptions.add_argument("--incognito")
            if(self.__config.getHeadlessMode()):
                chromeoptions.add_argument("--headless")
            if (self.__config.getLang()):
                chromeoptions.add_argument("--lang={}".format(self.__config.getLang()))
            if(self.__config.getExtensions()):
                for ext in self.__config.getExtensions():
                    chromeoptions.add_extension("./core/extensions/{}/{}.crx".format(self.__config.getBrowser(),ext))
            if (self.__config.getCapabilities()):
                for k, v in self.__config.getCapabilities().items():
                    chromeoptions.set_capability(k, v)   
            self.__driver = webdriver.Chrome(executable_path=self.__config.getDriverPath(),options=chromeoptions)
        elif(self.__config.getBrowser() == "ie"):
            self.__driver = webdriver.Ie(executable_path=self.__config.getDriverPath(),timeout=self.__config.getDefaultWait())
        elif(self.__config.getBrowser() == "edge"):
            self.__driver = webdriver.Edge(executable_path=self.__config.getDriverPath())
        else:
            raise AttributeError('Invalid Browser')
        if (self.__config.getHeadlessMode()):
            self.__driver.set_window_size(self.__config.getWindowSize()['X'],self.__config.getWindowSize()['Y'])
        else:
            self.__driver.maximize_window()
        self.__driver.set_page_load_timeout(self.__config.getDefaultWait())
        self.__driver.implicitly_wait(self.__config.getDefaultWait())
        self.__driver.get(self.__config.getUrlApp())
        
        return self.__driver