from selenium import webdriver
from ..pages.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        base_URL = "http://localhost:8084/console/login"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_URL)

        login_page = LoginPage(driver)
        login_page.login("admin", "admin")

        self.assertTrue(login_page.verifyPageTitlePresent())
        self.assertEquals(driver.title, "HMS: Global Prefs")

        driver.quit()
