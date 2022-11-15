import os
import unittest
import time
from selenium import webdriver

from pages.add_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayerPage(unittest.TestCase):
    s = Service(DRIVER_PATH)
    driver = None

    os.chmod(DRIVER_PATH, 755)

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        # Log in to the system and load the dashboard page
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user07@getnada.com")
        user_login.fill_in_password_with_text("Test-1234")
        user_login.click_on_sign_in_button()
        time.sleep(3)

        # Click on Add player link and load the page
        add_player = AddPlayer(self.driver)
        add_player.click_on_add_player_link()
        add_player.check_page_title()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
