import os
import unittest
import time
from selenium import webdriver

from pages.add_player import AddPlayer
from pages.login_page import LoginPage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestAddPlayerPage(unittest.TestCase):
    s = Service(DRIVER_PATH)
    driver = None

    add_player_page_url_xpath = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    os.chmod(DRIVER_PATH, 755)

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        # Log in to the system and load the dashboard page
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user07@getnada.com")
        user_login.fill_in_password_with_text("Test-1234")
        user_login.click_on_sign_in_button()

    def test_add_player(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_add_player_link()
        add_player.check_page_title()
        add_player.complete_fields()
        add_player.click_submit_button()
        add_player.find_added_player_alert(self.driver)
        add_player.wait_for_redirection(self.add_player_page_url_xpath)

    def test_correctness_of_data(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_add_player_link()
        add_player.check_page_title()
        add_player.complete_fields()
        add_player.click_submit_button()
        add_player.check_correctness_of_profile_data(self.driver)

    def test_age_field_day_validation(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_add_player_link()
        add_player.check_page_title()
        add_player.complete_mandatory_fields_enter_incorrect_day()
        add_player.click_submit_button()
        add_player.find_error_alert(self.driver)


    def test_age_field_year_validation(self):
        add_player = AddPlayer(self.driver)
        add_player.click_on_add_player_link()
        add_player.check_page_title()
        add_player.complete_mandatory_fields_enter_incorrect_year()
        add_player.click_submit_button()
        add_player.find_error_alert(self.driver)


    @classmethod
    def tearDown(self):
        self.driver.quit()
