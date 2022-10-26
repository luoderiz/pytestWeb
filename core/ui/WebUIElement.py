import pytest
import traceback
from core.ui.BaseElement import BaseElement

from core.assertion.Assertion import Assertion
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class WebUIElement (BaseElement):

    """
        Class to handle the Selenium WebElement.
        This class offer all methods of WebElement with exception handle.
        This class inherits from BaseElement.
    """

    def __init__(self, byType="", locator="", parentFrame=None):
        """
            WebUIElement constructor receives a By object and a locator string to perform actions over this element 
            and a parentFrame.
            :param byTipe : By
            :param locator: str
            :param parentFrame: FrameElement
        """
        self._BaseElement__byType = byType
        self._BaseElement__element = locator
        self._BaseElement__parentFrame = parentFrame
        

    def click(self, withWait=False):
        """
            Perform a click action over the current element.
        """
        try:
            self._BaseElement__get(withWait).click()
        except ElementClickInterceptedException as cie:
            print("Element Click Intercepted Exception: {}\n{}".format(self._BaseElement__element,cie))
            Assertion.assertTrue("Unable to click on {} element because it overlaps".format(self._BaseElement__element), False)
        except StaleElementReferenceException as ser:
            print("Stale Element Reference Exception: {}\n{}".format(self._BaseElement__element,ser))
        except Exception as e:
            pytest.fail(e.args[0],True)

    def isClickable(self):
        """
            Search for the clickability of the current element.
            :return: bool
        """
        try:
            return self._BaseElement__clickable()
        except Exception as e:
            pytest.fail(e.args[0],True)

    def isDisplayed(self):
        """
            Search for the visibility of the current element.
            :return: bool
        """
        try:
            return self._BaseElement__exist(visible=True)
        except Exception as e:
            pytest.fail(e.args[0],True)

    def isPresent(self, withWait=True):
        """
            Search for the presence of the current element.
            :param withWait: bool
            :return: bool
        """
        try:
            return self._BaseElement__exist(withWait=withWait)
        except Exception as e:
            pytest.fail(e.args[0],True)

    def isNotDisplayed(self):
        """
            Search for the invisiblity or not presence of the current element.
            :return: bool
        """
        try:
            return self._BaseElement__disappear()
        except Exception as e:
            pytest.fail(e.args[0],True)

    def mouseOver(self):
        """
            Perform a 'mouse over' the current element. This element must be visible on the screen.
            This method doesn't work on Internet Explorer
        """
        action = ActionChains(self._BaseElement__getDriver()).move_to_element(self._BaseElement__get())
        action.perform()

    def submit(self):
        """
            Perform the submit action in the current element. 
            If this element is part of a form this action will send the current form like the button submit has been clicked
        """
        self._BaseElement__get().submit()

    def clear(self):
        """
            Clear a textbox field
        """
        self._BaseElement__get().clear()

    def setText(self, text):
        """
            Send the text receive into a textbox
            :param text: str
        """
        self._BaseElement__get().send_keys(text)

    def getText(self):
        """
            Get the text of a element
            :return: str
        """
        return self._BaseElement__get().text

    def getAttribute(self,attribute):
        """
            Get the text of attribute param
            :param attribute: str
            :return: str 
        """
        return self._BaseElement__get().get_attribute(attribute)

    def scrollUntilThis(self):
        """
            Perform the scroll action until the visibility of current element
        """
        self._BaseElement__getDriver().execute_script("arguments[0].scrollIntoView({block: 'center'});", self._BaseElement__get())

    def clickByJavaScript(self):
        """
            Perform a click action over the current element using JavaScript
        """
        try:
            self._BaseElement__getDriver().execute_script("arguments[0].click();",self._BaseElement__get())
        except StaleElementReferenceException as ser:
            print("Stale Element Reference Exception: {}\n{}".format(self._BaseElement__element,ser))

    def getElementsList(self):
        """
            Returns a list elements
            :return: list
        """
        if self._BaseElement__getList():
            return self._BaseElement__getList()
        else:
            return []

    def isTextInElement(self, text):
        """
            Search for :text: in current element.
            :return: bool
        """
        return self._BaseElement__waitForTextInElement(text)

    def selectOption(self, opt, by="text"):
        """
            Selects an option in a combobox element.
            It can select by visible text, value or index.
            :param opt: str|int, option to select.
            :param by: str, way to select.
            :return: bool, True if success.
        """
        select = Select(self._BaseElement__get())
        try:
            if (by == "text"):
                select.select_by_visible_text(opt)
                return True
            elif (by == "value"):
                select.select_by_value(opt)
                return True
            elif (by == "index"):
                select.select_by_index(opt)
                return True
            else:
                raise NotImplementedError("Select by <{}> is not implemented".format(by))
        except NoSuchElementException as ne:
            print("No Such Element Exception: {}\n{}".format(self._BaseElement__element,ne))
            return False
        except NotImplementedError as ni:
            print("Not Implemented Error: {}".format(ni))
            return False