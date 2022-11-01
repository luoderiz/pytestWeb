from pytest_bdd import given, when, then, scenarios
from steps import LoginSteps as Login
from pages import LoginPage as LoginPage

scenarios('../features/Login.feature')


@given("I am in automationtesting site")
def navigateAutomationTestingSite():
    Login.LoginSteps.navigateSite()


@given("I click on My Account Menu")
def clickMyAccountMenu():
    Login.click(LoginPage.getMyAccountMenu())


@when("I enter my valid existing username <username> in the Login Textbox")
def enterValidUsername(username):
    Login.enterUsername(username)


@when("I enter my valid password <password> in the Login Textbox")
def enterValidPassword(password):
    Login.enterPassword(password)


@when("I click on Login Button")
def clickLoginButton():
    Login.click(LoginPage.getLoginButton())


@then("I am redirected to My Account Home Page")
def verifySuccessLogin():
    Login.verifyLogin()

