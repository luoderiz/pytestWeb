from pages import ExamplePage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion

class ExampleSteps(BaseStep):

    def loginButtonIsDisplayed(self):
        Assertion.assertTrue('Logo is not displayed', page.getLoginButton().isDisplayed())
        return self