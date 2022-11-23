from pages.base_page import BasePage
import time


class AddPlayer(BasePage):
    add_player_link_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title_add_player = "Add player"

    email_field_xpath = '//*[@name="email"]'
    name_field_xpath = '//*[@name="name"]'
    surname_field_xpath = '//*[@name="surname"]'
    phone_field_xpath = '//*[@name="phone"]'
    weight_field_xpath = '//*[@name="weight"]'
    height_field_xpath = '//*[@name="height"]'
    age_field_xpath = '//*[@name="age"]'
    leg_field_xpath = '//*[@id="mui-component-select-leg"]'
    right_leg_xpath = '//*[@id="menu-leg"]/div[3]/ul/li[1]'
    leg_xpath = '//*[@id="leg"]'
    club_field_xpath = '//*[@name="club"]'
    level_field_xpath = '//*[@name="level"]'
    mainPosition_field_xpath = '//*[@name="mainPosition"]'
    secondPosition_field_xpath = '//*[@name="secondPosition"]'
    district_field_xpath = '//*[@id="mui-component-select-district"]'
    lower_silesia_xpath = '//*[@data-value="dolnoslaskie"]'
    district2_xpath = '//*[@id="district"]'
    achievements_field_xpath = '//*[@name="achievements"]'
    languages_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]'
    languages_field_xpath = '//*[@name="languages[0]"]'
    laczyPilka_field_xpath = '//*[@name="webLaczy"]'
    web90_field_xpath = '//*[@name="web90"]'
    webFB_field_xpath = '//*[@name="webFB"]'
    webYT_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[19]/button'
    webYT_field_xpath = '//*[@name="webYT[0]"]'
    submit_button_xpath = '//*[@type="submit"]'

    button_with_user_profile_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]'
    page_heading_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span'

    message_about_redirection_xpath = '//*[@id="czlwh5r1ht"]/div[1]'

    def click_on_add_player_link(self):
        self.click_on_the_element(self.add_player_link_xpath)

    def check_page_title(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title_add_player

    email = "example@google.com"
    name = "John"
    surname = "Doe"
    phone = "+48123456789"
    weight = "70"
    height = "170"
    age = "12.04.1970"
    age_incorrect_day = "99.04.1970"
    age_incorrect_year = "12.04.3333"
    age_reversed = "1970-04-12"
    club = "Real Madrid"
    level = "Professional"
    mainPosition = "Quarterback"
    secondPosition = "Goalkeeper"
    achievement = "Example achievement"
    languages = "Ukrainian"
    laczyPilka = "Example text"
    ninetyMinutes = "Example 90 minutes"
    facebook = "example.facebook.com"
    youtube = "example@youtube.com"
    leg = "right"
    district = "dolnoslaskie"


    def complete_fields(self):
        self.field_send_keys(self.email_field_xpath, self.email)
        self.field_send_keys(self.name_field_xpath, self.name)
        self.field_send_keys(self.surname_field_xpath, self.surname)
        self.field_send_keys(self.phone_field_xpath, self.phone)
        self.field_send_keys(self.weight_field_xpath, self.weight)
        self.field_send_keys(self.height_field_xpath, self.height)
        self.field_send_keys(self.age_field_xpath, self.age)
        self.click_on_the_element(self.leg_field_xpath)
        self.click_on_the_element(self.right_leg_xpath)
        self.field_send_keys(self.club_field_xpath, self.club)
        self.field_send_keys(self.level_field_xpath, self.level)
        self.field_send_keys(self.mainPosition_field_xpath, self.mainPosition)
        self.field_send_keys(self.secondPosition_field_xpath, self.secondPosition)
        self.click_on_the_element(self.district_field_xpath)
        self.click_on_the_element(self.lower_silesia_xpath)
        self.field_send_keys(self.achievements_field_xpath, self.achievement)
        self.click_on_the_element(self.languages_button_xpath)
        self.field_send_keys(self.languages_field_xpath, self.languages)
        self.field_send_keys(self.laczyPilka_field_xpath, self.laczyPilka)
        self.field_send_keys(self.web90_field_xpath, self.ninetyMinutes)
        self.field_send_keys(self.webFB_field_xpath, self.facebook)
        self.click_on_the_element(self.webYT_button_xpath)
        self.field_send_keys(self.webYT_field_xpath, self.youtube)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)



    def check_correctness_of_profile_data(self, driver):
        time.sleep(5)
        self.check_correctness_of_data(driver, self.email_field_xpath, self.email)
        self.check_correctness_of_data(driver, self.name_field_xpath, self.name)
        self.check_correctness_of_data(driver, self.surname_field_xpath, self.surname)
        self.check_correctness_of_data(driver, self.phone_field_xpath, self.phone)
        self.check_correctness_of_data(driver, self.weight_field_xpath, self.weight)
        self.check_correctness_of_data(driver, self.height_field_xpath, self.height)
        self.check_correctness_of_data(driver, self.age_field_xpath, self.age_reversed)
        self.check_correctness_of_data(driver, self.leg_xpath, self.leg)
        self.check_correctness_of_data(driver, self.club_field_xpath, self.club)
        self.check_correctness_of_data(driver, self.level_field_xpath, self.level)
        self.check_correctness_of_data(driver, self.mainPosition_field_xpath, self.mainPosition)
        self.check_correctness_of_data(driver, self.secondPosition_field_xpath, self.secondPosition)
        self.check_correctness_of_data(driver, self.district2_xpath, self.district)
        self.check_correctness_of_data(driver, self.achievements_field_xpath, self.achievement)
        self.check_correctness_of_data(driver, self.languages_field_xpath, self.languages)
        self.check_correctness_of_data(driver, self.languages_field_xpath, self.languages)
        self.check_correctness_of_data(driver, self.laczyPilka_field_xpath, self.laczyPilka)
        self.check_correctness_of_data(driver, self.web90_field_xpath, self.ninetyMinutes)
        self.check_correctness_of_data(driver, self.webFB_field_xpath, self.facebook)
        self.check_correctness_of_data(driver, self.webYT_field_xpath, self.youtube)

    def complete_mandatory_fields_enter_incorrect_day(self):
        self.field_send_keys(self.email_field_xpath, self.email)
        self.field_send_keys(self.name_field_xpath, self.name)
        self.field_send_keys(self.surname_field_xpath, self.surname)
        self.field_send_keys(self.age_field_xpath, self.age_incorrect_day)
        self.field_send_keys(self.mainPosition_field_xpath, self.mainPosition)

    def complete_mandatory_fields_enter_incorrect_year(self):
        self.field_send_keys(self.email_field_xpath, self.email)
        self.field_send_keys(self.name_field_xpath, self.name)
        self.field_send_keys(self.surname_field_xpath, self.surname)
        self.field_send_keys(self.age_field_xpath, self.age_incorrect_year)
        self.field_send_keys(self.mainPosition_field_xpath, self.mainPosition)
