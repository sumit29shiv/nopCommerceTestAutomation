from selenium.webdriver.common.by import By



class ElementUtil():

    def __init__(self,driver):
        self.driver = driver

    def getPageTitle(self):
        return self.driver.title

    def getElement(self,byLocator):
        return self.driver.find_element(*byLocator)

    def doClear(self,byLocator):
        self.getElement(byLocator).clear()

    def doClick(self,byLocator):
        self.getElement(byLocator).click()

    def doSendKeys(self,byLocator,value):
       self.getElement(byLocator).send_keys(value)


    def isElementVisible(self,byLocator):
        return self.getElement(byLocator).is_displayed()

    def getElementText(self,byLocator):
        return self.getElement(byLocator).text



