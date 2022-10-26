from pages import GoogleSearchPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion

class GoogleSearchSteps(BaseStep):

    def enterSearchCriteria(cls, text):
        driverElem = page.inputSearchId()
        driverElem.setText(text)


    def clickSearchButton(cls):
        driverElem = page.searchXpath()
        driverElem.click()


    def verifyResult(self, text):
        driverElem = page.STATS_ID()
        Assertion.assertTrue("Busqueda no encontrada", driverElem.isTextInElement(text))
        return self
