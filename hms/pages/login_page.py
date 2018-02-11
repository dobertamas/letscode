from selenium.webdriver.common.by import By
from ..base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _username_field = "username"
    _password_field = "password"
    _login_button = "signin"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enter_username(self, email):
        self.sendKeys(email, self._username_field, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        #self.clickLoginLink()
        self.enter_username(email)
        self.enterPassword(password)
        self.clickLoginButton()
