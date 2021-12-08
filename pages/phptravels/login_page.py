import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators
from base.page_base import PageBase


class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Expanding account menu")
    def expand_account_menu(self):
        self.driver.find_element(*LogInLocators.user_account_menu).click()

    @allure.step("Opening login page")
    def open_login_page(self):
        self.driver.find_element(*LogInLocators.login_link).click()

    @allure.step("Login with email: '1'")
    def set_user_inputs(self, email, password):
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(
            *LogInLocators.password_input).send_keys(password, Keys.ENTER)

    @allure.step("Logout")
    def logout(self):
        self.driver.find_element(*LogInLocators.logout_link).click()
