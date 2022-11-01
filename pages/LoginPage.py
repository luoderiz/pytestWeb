from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


def getMyAccountMenu():
    return UIElement(By.ID, 'menu-item-50')


def getLoginButton():
    return UIElement(By.XPATH, '//input[@name="login"]')


def getUsernameTextbox():
    return UIElement(By.ID, 'username')


def getPasswordTextbox():
    return UIElement(By.ID, 'password')


def getErrorMessage():
    return UIElement(By.XPATH, '//ul[@class="woocommerce-error"]')


def getMyAccountHomePageUrl():
    return 'https://practice.automationtesting.in/my-account/'

