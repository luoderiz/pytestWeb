from pytest_bdd import then, scenarios, given, when
from steps.GoogleSearchSteps import GoogleSearchSteps as googleSearch

scenarios('../features/GoogleSearch.feature')


@given('The client is in google page')
def validatePage():
    googleSearch().getTitle()


@when('The client search for word <text>')
def inputSearch(text):
    googleSearch().enterSearchCriteria(text)
    googleSearch().clickSearchButton()


@then('The client verify that results <text> are shown properly')
def verifyResult(text):
    googleSearch().verifyResult(text)

def teardown():
    googleSearch().closeBrowser()