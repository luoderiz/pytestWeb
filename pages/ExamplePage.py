from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getLoginButton():
    return UIElement(By.ID,'login-button')
