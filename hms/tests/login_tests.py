from selenium import webdriver
from ..pages.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    base_URL = "http://localhost:8084/console/login"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_URL)

    login_page = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.login_page.login("admin", "admin")

        self.assertTrue(self.login_page.verifyPageTitlePresent())
        self.assertEquals(self.driver.title, "HMS: Global Prefs")

        # driver.quit()

    @pytest.mark.run(order=2)
    def test_inValid_login(self):
        pass
