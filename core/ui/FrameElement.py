from core.ui.WebUIElement import WebUIElement as UIElement

class FrameElement(UIElement):

    """
        FrameElement is a class to handler a WebElement that is Parent of other Elements like Frame or iFrames.
        This class inherits from WebUIElement.
    """

    def __init__(self, byType="", locator="", parent=None):
        """
            FrameElement constructor receives a By object and a locator string to perform actions over this element 
            and a parentFrame.
            :param byTipe : By
            :param locator: str
            :param parentFrame: FrameElement
        """
        super().__init__(byType,locator,parent)