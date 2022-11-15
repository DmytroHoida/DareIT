from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
    login_url = ("https://scouts-test.futbolkolektyw.pl/en")
    expected_title = "Scouts panel - sign in"
    expected_text = "Scouts Panel"
    text_box_xpath = '//*[@id="__next"]/form/div/div[1]/h5'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def fill_in_password_with_text(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_page_title(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_text_above_login_field(self):
        self.assert_element_text(self.driver, self.text_box_xpath, self.expected_text)

