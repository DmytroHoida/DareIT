from pages.base_page import BasePage


class AddMatch(BasePage):

    # Xpath to the whole form on the page
    add_match_form_xpath = '//form'

    # Xpath to the title
    add_match_title_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[1]/div/span'

    # Xpath to My team field
    my_team_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label'
    my_team_field_xpath = '//input[@name="myTeam"]'

    # Xpath to Enemy team field
    enemy_team_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/label'
    enemy_team_field_xpath = '//input[@name="enemyTeam"]'

    # Xpath to My team score field
    my_team_score_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/label'
    my_team_score_field_xpath = '//input[@name="myTeamScore"]'

    # Xpath to Enemy team score field
    enemy_team_score_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label'
    enemy_team_score_field_xpath = '//input[@name="enemyTeamScore"]'

    # Xpath to Date field
    date_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/label'
    date_field_xpath = '//input[@name="date"]'

    # Xpath to Match at home / Match out home select field
    match_at_or_out_home_select_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]'

    # Xpath to T-shirt color field
    tshirt_color_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/label'
    tshirt_color_field_xpath = '//input[@name="tshirt"]'

    # Xpath to League field
    league_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[8]/div/label'
    league_field_xpath = '//input[@name="league"]'

    # Xpath to Time played field
    time_played_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/label'
    time_played_field_xpath = '//input[@name="timePlayed"]'

    # Xpath to Number field
    number_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/label'
    number_field_xpath = '//input[@name="number"]'

    # Xpath to Web match field
    web_match_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/label'
    web_match_field_xpath = '//input[@name="webMatch"]'

    # Xpath to General field
    general_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div/label'
    general_field_xpath = '//input[@name="general"]'

    # Xpath to Rating field
    rating_label_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/label'
    rating_field_xpath = '//input[@name="rating"]'

    # Xpath to Submit and Clear buttons
    submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]'
    clear_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]'

    pass