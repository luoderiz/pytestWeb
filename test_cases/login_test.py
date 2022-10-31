from pytest_bdd import given, when, then, scenarios
from steps.LoginSteps import LoginSteps as login
from pages import LoginPage as loginPage

scenarios('../features/Login.feature')


@given("I am in automationtesting site")
def navigateAutomationTestingSite():
    pingo = Login()
    login.navigateSite(self=)


@given("I click on My Account Menu")
def clickMyAccountMenu():
    login.click(loginPage.getMyAccountMenu())


@when("I enter my valid existing username <username> in the Login Textbox")
def enterValidUsername(username):
    login.enterUsername(username)


@when("I enter my valid password <password> in the Login Textbox")
def enterValidPassword(password):
    login.enterPassword(password)


@when("I click on Login Button")
def clickLoginButton():
    login.click(loginPage.getLoginButton())


@then("I am redirected to My Account Home Page")
def verifySuccessLogin():
    login.verifyLogin()