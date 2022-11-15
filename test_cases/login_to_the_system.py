import os
import unittest
import time
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestLoginPage(unittest.TestCase):
    s = Service(DRIVER_PATH)
    driver = None

    os.chmod(DRIVER_PATH, 755)

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.check_page_title()
        user_login.check_text_above_login_field()
        user_login.type_in_email("user07@getnada.com")
        user_login.fill_in_password_with_text("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_page_title()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()