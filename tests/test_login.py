import time

import pytest

from tests.baseTest import BaseTest as bt
from utils.constants import Constants


@pytest.mark.usefixtures("setUp")
class Test_NoPCommerce_001_Login(bt):

    def test_verifyPageTitle(self):
        actualTitle = self.loginPage.getLoginPageTitle()
        assert actualTitle==Constants.LOGIN_PAGE_TITLE

    def test_verifyLogin(self):
        name = self.loginPage.doLogin(self.userName,self.password)
        print("Account name is:",name)
        assert name == Constants.ACCOUNT_NAME
