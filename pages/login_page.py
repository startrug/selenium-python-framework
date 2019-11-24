from selenium.webdriver.common.keys import Keys

from locators.locators import LogInLocators


class LogInPage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://www.phptravels.net/")

    def open_login_page(self):
        self.driver.find_element(*LogInLocators.user_account_menu).click()
        self.driver.find_element(*LogInLocators.login_link).click()

    def set_user_inputs(self, email, password):
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(*LogInLocators.password_input).send_keys(password, Keys.ENTER)


