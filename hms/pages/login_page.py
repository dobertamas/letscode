from ..base.selenium_driver import SeleniumDriver
from ..utilities.custom_logger import *


class LoginPage(SeleniumDriver):
    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _username_field = "username"
    _password_field = "password"
    _login_button = "signin"
    _title = "title"
    _page_title = "HMS: Global Prefs"

    def enter_username(self, email):
        self.sendKeys(email, self._username_field, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="name")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.enter_username(email)
        self.enterPassword(password)
        # time.sleep(30)
        self.clickLoginButton()

    def verifyPageTitlePresent(self):
        return self.isElementPresent(self._title, locatorType="tag")
