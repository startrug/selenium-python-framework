import allure
from selenium.webdriver.common.keys import Keys
from locators.locators import LogInLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec



class LogInPage:
    def __init__(self, driver):
        self.driver = driver
        #self.logger = logging.getLogger(__name__)

    search_input = By.CSS_SELECTOR, "input[name='q']"
    contact_link = "[data-target='#exampleModal']"
    #contact_link = By.LINK_TEXT, "Contact"

    @allure.step("Opening demoblaze.com website")
    def open_page(self):
        #self.logger.info("Opening phptravels.net website")
        self.driver.get("https://demoblaze.com/")

    @allure.step("Provide text into search input")
    def go_to_contact(self):
        # el = ec.visibility_of(self.driver.find_element(self.contact_link))
        e = self.driver.find_element_by_css_selector(self.contact_link)
        e.click()

    @allure.step("Provide text into search input")
    def search(self, text):
        self.driver.find_element(self.search_input).send_keys(text, Keys.ENTER)

    @allure.step("Expanding account menu")
    def expand_account_menu(self):
        #self.logger.info("Expanding account menu")
        self.driver.find_element(*LogInLocators.user_account_menu).click()

    @allure.step("Opening login page")
    def open_login_page(self):
        #self.logger.info("Opening login page")
        self.driver.find_element(*LogInLocators.login_link).click()

    @allure.step("Login with email: '1'")
    def set_user_inputs(self, email, password):
        self.logger.info("Setting user email to {}".format(email) + " and password")
        self.driver.find_element(*LogInLocators.email_input).click()
        self.driver.find_element(*LogInLocators.email_input).send_keys(email)
        self.driver.find_element(*LogInLocators.password_input).click()
        self.driver.find_element(*LogInLocators.password_input).send_keys(password, Keys.ENTER)

    @allure.step("Logout")
    def logout(self):
        self.logger.info("Logout")
        self.driver.find_element(*LogInLocators.logout_link).click()



