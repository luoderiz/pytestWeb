from core.driver.WebDriver import WebDriver as Driver
from core.config.ConfigHelper import ConfigHelper

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from core.assertion.Assertion import Assertion
from abc import ABC
import allure, datetime


class BaseStep (ABC):

    """
        BasePage is a Abstract class that offer somes methods to do somes actions without an WebUIElement
    """

    def __getDriver(self):
        """
            Call for the instance of WebDriver to return it.
            :return: WebDriver
        """
        return Driver.getInstance()

    def __getDriverWait(self):
        """
            Call for Selenium WebDriver Wait to create a handle of elements with a wait. This wait is configured in the file config.json
            :return: WebDriverWait
        """
        return WebDriverWait(self.__getDriver(),ConfigHelper.getInstance().getDefaultWait())

    @allure.step
    def getTitle(self):
        """
            A method to get the title for the current page.
            :return: str
        """
        return Driver.getInstance().title

    @allure.step
    def goToUrl(self,url=""):
        """
            A method to go at specify URL.
            :param url: str
        """
        Driver.getInstance().get(url)
        return self

    @allure.step
    def getUrl(self):
        """
            A method to get the url address for the current page.
            :return: str
        """
        return Driver.getInstance().current_url

    @allure.step
    def verifyUrlContains(self,url="",errorMsg=""):
        """
            Verify Url from the current page with the Expected value

            :param url: str
            :return: self
        """
        Driver.getInstance()
        Assertion().assertTrue('Url from the current page not contains [{}]. {}.'.format(url, errorMsg) ,url in self.getUrl())
        return self

    @allure.step
    def waitForUrlContains(self,url="",errorMsg=""):
        """
            Wait until defined timeout and verify Url from the current page with the Expected value

            :param url: str
            :return: self
        """
        try:
            self.__getDriverWait().until(expected_conditions.url_contains(url))
        except:
            Assertion.assertTrue("Url from the current page not contains [{}]. {}.".format(url, errorMsg), False)
        return self

    @allure.step
    def closeBrowser(self):
        """
            A method to close the current Browser
        """
        Driver.closeDriver()

    @allure.step
    def verifyPageTitle(self,titleExpected):
        """
            Verify Title from the current page with the Expected value

            :param titleExpected: str
            :return: self
        """
        Assertion().assertEquals(expectedValue=titleExpected,actualValue=self.getTitle())
        return self


    @allure.step
    def takeScreenshot(self,name=str(datetime.datetime.now())):
        """
            Take a screenshot in PNG format and attach it into allure report.
            Receive a name for the image. By default set the current timestamp for the name.

            :params name: str
        """
        allure.attach(Driver.getInstance().get_screenshot_as_png(),name,attachment_type=allure.attachment_type.PNG)
        return self

    @allure.step
    def acceptAlert(self):
        """
            Accept the current dialog displayed on the browser
        """
        Driver.getInstance().switch_to.alert.accept()
        return self

    @allure.step
    def declineAlert(self):
        """
            Cancel the current dialog displayed on the browser
        """
        Driver.getInstance().switch_to.alert.dismiss()
        return self
    
    @allure.step
    def __getAlertMessage(self):
        """
            Get message from the current dialog displayed on the browser
        """
        return Driver.getInstance().switch_to.alert.text

    @allure.step
    def __setTextOnAlertMessage(self, message):
        """
            Set text in the current dialog displayed on the browser
        """
        Driver.getInstance().switch_to.alert.send_keys(message)
        
    @allure.step
    def sendKey(self,key):
        """
            Perform send the key action in the current driver. 
        """
        action = ActionChains(Driver.getInstance()).send_keys(key)
        action.perform()

    def refresh(self):
        """
            Perform refresh actual page. 
        """
        Driver.getInstance().refresh()