from pages.base_page import BasePage
import time


class Dashboard(BasePage):

    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def check_page_title(self):
        self.wait_for_element_to_be_clickable(self.shortcuts_container_add_player_link_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title



    # Xpaths to 4 boxes with counts at the top of the page
    four_count_boxes = '//*[@id="__next"]/div[1]/main/div[2]'
    players_count_box_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[1]'
    matches_count_box_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[2]'
    reports_count_box_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[3]'
    events_count_box_xpath = '//*[@id="__next"]/div[1]/main/div[2]/div[4]'

    # Xpaths to Scout panel container and its elements
    scouts_panel_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]'
    scouts_panel_logo_xpath = '// div[@title="Logo Scouts Panel"]'
    scouts_panel_title_xpath = '//h2[text()="Scouts Panel"]'
    scouts_panel_description_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[2]/p'
    scouts_panel_dev_team_contact_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]'

    # Xpaths to Shortcuts container
    shortcuts_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div'
    shortcuts_container_title_xpath = '//*[text()="Shortcuts"]'
    shortcuts_container_add_player_link_xpath = '//*[text()="Add player"]'

    # Xpaths to Activity container
    activity_container_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]'
    activity_container_title_xpath = '//*[text()="Activity"]'
    # Last created player
    activity_container_last_created_player_textbox_xpath = '//*[text()="Last created player"]'
    activity_container_last_created_player_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]'
    # Last updated player
    activity_container_last_updated_player_textbox_xpath = '//*[text()="Last updated player"]'
    activity_container_last_updated_player_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[2]'
    # Last created match
    activity_container_last_created_match_textbox_xpath = '//*[text()="Last created match"]'
    activity_container_last_created_match_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[3]'
    # Last updated match
    activity_container_last_updated_match_textbox_xpath = '//*[text()="Last updated match"]'
    activity_container_last_updated_match_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[4]'
    # Last updated report
    activity_container_last_updated_report_textbox_xpath = '//*[text()="Last updated report"]'
    activity_container_last_updated_report_link_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[5]'

    # Xpaths to the menu bar
    menu_scouts_panel_text_box_xpath = '//h6[text()="Scouts Panel"]'
    menu_main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]'
    menu_players_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]'
    menu_language_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]'
    menu_sign_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]'
    # Burger menu
    burger_menu_button_xpath = '//*[@id="__next"]/div[1]/header/div/button'
    burger_menu_main_page_button_xpath = '/html/body/div[2]/div[3]/div/ul[1]/div[1]'
    burger_menu_players_button_xpath = '/html/body/div[2]/div[3]/div/ul[1]/div[2]'
    burger_menu_language_button_xpath = '/html/body/div[2]/div[3]/div/ul[1]/div[3]'
    burger_menu_sign_out_button_xpath = '/html/body/div[2]/div[3]/div/ul[1]/div[4]'

    pass
