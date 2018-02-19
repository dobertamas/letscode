from selenium import webdriver
import unittest
# from ..pages.login_page import LoginPage
from hms.pages.login_page import LoginPage


class LoginTests(unittest.TestCase):
    base_URL = "http://localhost:8084/console/login"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_URL)

    login_page = LoginPage(driver)

    def test_valid_login(self):
        self.login_page.login("admin", "admin")

        self.assertTrue(self.login_page.verifyPageTitlePresent())
        self.assertEquals(self.driver.title, "HMS: Global Prefs")

        self.driver.quit()

    def test_inValid_login(self):
        pass
