from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
class BasePage:

    def init_driver(self,browser):
        print("Running tests in",browser+"....")
        if(browser=="chrome"):
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif(browser=="firefox"):
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif(browser=="safari"):
            self.driver = webdriver.Safari()
        else:
            print("Please provide correct browser",browser)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()

        return self.driver

