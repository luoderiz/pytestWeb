from core.driver.WebDriver import WebDriver
import allure, pytest, datetime

class Assertion():

    """
        Class to handle Assertions to do verifications in our Test Cases.
    """
    @classmethod
    def assertTrue(cls,failedMessage,value):
        """
            Verify that the input value is True. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :failedMessage: str
            :value: bool
        """
        try:
            assert True == value
        except:
            cls.__on_failure_screesnshot()
            pytest.fail(failedMessage,False)

    @classmethod
    def assertFalse(cls,failedMessage,value):
        """
            Verify that the input value is False. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :failedMessage: str
            :value: bool
        """
        try:
            assert False == value
        except:
            cls.__on_failure_screesnshot()
            pytest.fail(failedMessage,False)

    @classmethod
    def assertEquals(cls,failedMessage='', expectedValue=None, actualValue=None):
        """
            Verify that the value of the inputs is Equals. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :expectedValue: Obj
            :actualValue: Obj
        """
        try:
            assert expectedValue == actualValue
        except:
            cls.__on_failure_screesnshot()
            pytest.fail("{}. Expected: '{}' but Actual is: '{}'".format(failedMessage,expectedValue,actualValue),False)

    @classmethod
    def assertNotEquals(cls,failedMessage='', expectedValue=None, actualValue=None):
        """
            Verify that the value of the inputs is Not Equals. Otherwise, the Assertion will fail and take a ScreenShot automatically
            and add the Allure report the failed message

            :expectedValue: Obj
            :actualValue: Obj
        """
        try:
            assert expectedValue != actualValue
        except:
            cls.__on_failure_screesnshot()
            pytest.fail("Equals. Expected: '{}' but Actual is: '{}'. {}".format(expectedValue,actualValue,failedMessage),False)

    @classmethod
    def __on_failure_screesnshot(cls):
        """
            Private method to take a Screenshot if an Assertion fails.
        """
        allure.attach(WebDriver.getInstance().get_screenshot_as_png(),str(datetime.datetime.now()),attachment_type=allure.attachment_type.PNG)