from pytest_bdd import then, scenarios
from steps.ExampleSteps import ExampleSteps as example

scenarios('../features/Example.feature')

@then('valida el boton de login')
def validateLogo():
    example().loginButtonIsDisplayed()

def teardown():
    example().closeBrowser()