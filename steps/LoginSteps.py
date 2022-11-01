from core.assertion.Assertion import Assertion
from core.config.ConfigHelper import ConfigHelper
from core.ui.WebUIElement import WebUIElement
from pages import LoginPage as loginPage
from core.steps.BaseSteps import BaseStep


class LoginSteps(BaseStep):

    def navigateSite(self):
        appUrl = ConfigHelper.getUrlApp()
        BaseStep.goToUrl(self, url=appUrl)
        return self

    def click(self, element):
        WebUIElement.click(element)
        return self

    def enterUsername(self, username):
        textbox = loginPage.getUsernameTextbox()
        WebUIElement.setText(textbox, username)
        return self

    def enterPassword(self, password):
        loginPage.getPasswordTextbox().setText(self, password)
        return self

    def verifyLogin(self):
        Assertion.assertEquals('Login attempt failed', loginPage.getMyAccountHomePageUrl(), BaseStep.getUrl(self))
        return self
