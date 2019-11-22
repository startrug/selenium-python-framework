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
