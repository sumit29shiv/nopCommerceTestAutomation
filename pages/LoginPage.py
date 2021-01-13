from selenium.webdriver.common.by import By
from utils.ElementUtil import ElementUtil


class LoginPage():


    '''defining by locators(object repository)'''
    __userNameField = (By.XPATH,"//input[@id='Email']")
    __passwordField = (By.ID,"Password")
    __loginBtn = (By.XPATH,"//input[@value='Log in']")
    __logoutBtn = (By.XPATH,"Logout")
    __accountNameLinkText = (By.XPATH,"//li[@class='account-info']")

    def __init__(self,driver):
        self.driver = driver
        self.elementutil = ElementUtil(self.driver)


    def getLoginPageTitle(self):
        return self.elementutil.getPageTitle()


    def doLogin(self,uname,pwd):
        print("Login with",uname+" and",pwd)
        self.elementutil.doClear(self.__userNameField)
        self.elementutil.doSendKeys(self.__userNameField,uname)
        self.elementutil.doClear(self.__passwordField)
        self.elementutil.doSendKeys(self.__passwordField,pwd)
        self.elementutil.doClick(self.__loginBtn)
        if(self.elementutil.isElementVisible(self.__accountNameLinkText)):
            return self.elementutil.getElementText(self.__accountNameLinkText)
        else:
            return None









