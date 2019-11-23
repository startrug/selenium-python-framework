from selenium.webdriver.common.by import By


class HeaderTopLocators:
    user_account_menu = (By.XPATH, "//div[@class='dropdown dropdown-login dropdown-tab show']")
    login_link = (By.LINK_TEXT, "Login")
    sign_up_link = (By.XPATH, "Sign Up")


class HeaderNavLocators:
    home_page_link = (By.LINK_TEXT, "Home")
    blog_link = (By.LINK_TEXT, "Blog")
    offers_link = (By.LINK_TEXT, "Offers")
    company_menu = (By.LINK_TEXT, "Company")
    about_us_link = (By.LINK_TEXT, "About us")
    contact_us_link = (By.LINK_TEXT, "Contact Us")
    terms_and_conditions_link = (By.LINK_TEXT, "Company")
    privacy_policy_link = (By.LINK_TEXT, "Privacy Policy")


class SearchFormLocators:
    destination_inactive = (By.XPATH, "//span[text()='Search by Hotel or City Name')]")
    destination_input = (By.XPATH, "//div[@id='select2-drop']//input[@class='select2-input']")
    checkin_input = (By.XPATH, "//input[@id='checkin']")
    checkout_input = (By.XPATH, "//input[@id='checkout']")
    adults_plus = (
    By.XPATH, "//div[contains(@class,'col o2')]//button[contains(@class,'btn btn-white bootstrap-touchspin-up')]")
    adults_minus = (
    By.XPATH, "//div[contains(@class,'col o2')]//button[contains(@class,'btn btn-white bootstrap-touchspin-down')]")
    kids_plus = (
    By.XPATH, "//div[contains(@class,'col 01')]//button[contains(@class,'btn btn-white bootstrap-touchspin-up')]")
    kids_minus = (
    By.XPATH, "//div[contains(@class,'col 01')]//button[contains(@class,'btn btn-white bootstrap-touchspin-down')]")
    search_btn = (By.XPATH,
                  "//div[@class='col-md-2 col-xs-12 o1']//button[@class='btn btn-primary btn-block'][contains(text(),'Search')]")


class SearchTabsLocators:
    hotels_tab = (By.XPATH, "//a[@data-name='hotels']")
    flights_tab = (By.XPATH, "//a[@data-name='flights']")
    tours_tab = (By.XPATH, "//a[@data-name='tours']")
    transfer_tab = (By.XPATH, "//a[@data-name='transfer']")
    visa_tab = (By.XPATH, "//a[@data-name='visa']")
