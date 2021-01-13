import pytest

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage

class BaseTest():

    baseUrl = "https://admin-demo.nopcommerce.com/admin/"
    userName = "admin@yourstore.com"
    password = "admin"

    @pytest.fixture()
    def setUp(self):
        self.basePage = BasePage()
        self.driver = self.basePage.init_driver("chrome")
        self.loginPage = LoginPage(self.driver)
        self.driver.get(self.baseUrl)
        yield
        self.driver.quit()








