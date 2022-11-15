from pages.base_page import BasePage
import time

class AddPlayer(BasePage):
    add_player_link_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"

    def click_on_add_player_link(self):
        self.click_on_the_element(self.add_player_link_xpath)

    def check_page_title(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

