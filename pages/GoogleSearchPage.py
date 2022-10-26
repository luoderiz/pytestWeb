from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def inputSearchId():
    return UIElement(By.XPATH, "//input[@class='gLFyf gsfi']")

def searchXpath():
    return UIElement(By.NAME, "btnK")

def STATS_ID():
    return UIElement(By.ID, "rcnt")


