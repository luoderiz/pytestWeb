from core.assertion.Assertion import Assertion
from pages import LoginPage as loginPage
from core.steps.BaseSteps import BaseStep


class LoginSteps(BaseStep):

    def navigateSite(self):
        BaseStep.goToUrl(self, loginPage.getAutomationTestingSite())

    def click(self, element):
        element.click(self)

    def enterUsername(self, username):
        loginPage.getUsernameTextbox().setText(self, username)

    def enterPassword(self, password):
        loginPage.getPasswordTextbox().setText(self, password)

    def verifyLogin(self):
        Assertion.assertEquals('Login attempt failed', loginPage.getMyAccountHomePageUrl(), BaseStep.getUrl(self))
