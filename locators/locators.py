from selenium.webdriver.common.by import By


class SetLanguageLocators:
    lang_menu = (By.XPATH, "//a[@id='dropdownLangauge']")
    russian_lang = (By.XPATH, "//a[@id='ru']")
    farsi_lang = (By.XPATH, "//a[@id='fa']")
    german_lang = (By.XPATH, "//a[@id='de']")
    vietnamese_lang = (By.XPATH, "//a[@id='vi']")
    french_lang = (By.XPATH, "//a[@id='fr']")
    turkish_lang = (By.XPATH, "//a[@id='tr']")
    arabic_lang = (By.XPATH, "//a[@id='ar']")
    spanish_lang = (By.XPATH, "//a[@id='es']")
    english_lang = (By.XPATH, "//a[@id='en']")


class SetCurrencyLocators:
    currency_menu = (By.CSS_SELECTOR, "#dropdownCurrency")
    usd = (By.XPATH, "//a[text()='USD']")
    gbp = (By.XPATH, "//a[text()='GBP']")
    sar = (By.XPATH, "//a[text()='SAR']")
    eur = (By.XPATH, "//a[text()='EUR']")
    pkr = (By.XPATH, "//a[text()='PKR']")
    kwd = (By.XPATH, "//a[text()='KWD']")
    egp = (By.XPATH, "//a[text()='EGP']")
    jpy = (By.XPATH, "//a[text()='JPY']")
    inr = (By.XPATH, "//a[text()='INR']")
    cny = (By.XPATH, "//a[text()='CNY']")
    rub = (By.XPATH, "//a[text()='RUB']")
    vietnam_dong = (By.XPATH, "//a[@class='dropdown-item text-center'][contains(text(),'Vietnam')]")


class LogInLocators:
    user_account_menu = (By.XPATH, "//div[@class='dropdown dropdown-login dropdown-tab']")
    login_link = (By.LINK_TEXT, "Login")
    logout_link = (By.LINK_TEXT, "Logout")
    account_link = (By.LINK_TEXT, "Account")
    sign_up_link = (By.XPATH, "Sign Up")
    email_input = (By.XPATH, "//input[@placeholder='Email']")
    password_input = (By.XPATH, "//input[@placeholder='Password']")
    invalid_data_msg = (By.XPATH, "//div[@class='alert alert-danger']")


class HeaderNavLocators:
    home_page_link = (By.LINK_TEXT, "Home")
    blog_link = (By.LINK_TEXT, "Blog")
    offers_link = (By.LINK_TEXT, "Offers")
    company_menu = (By.LINK_TEXT, "Company")
    about_us_link = (By.LINK_TEXT, "About us")
    contact_us_link = (By.LINK_TEXT, "Contact Us")
    terms_and_conditions_link = (By.LINK_TEXT, "Company")
    privacy_policy_link = (By.LINK_TEXT, "Privacy Policy")


class SearchHotelsFormLocators:
    destination_inactive = (By.XPATH, "//span[text()='Search by Hotel or City Name']")
    destination_input = (By.XPATH, "//input[@class='select2-input select2-focused']")
    search_match = (By.XPATH, "//span[@class='select2-match']")
    checkin_input = (By.XPATH, "//input[@id='checkin']")
    checkout_input = (By.XPATH, "//input[@id='checkout']")
    adults_input_value = (By.XPATH, "//div[@class='col o2']//input[@name='adults']")
    kids_input_value = (By.XPATH, "//div[@class='col 01']//input[@name='children']")
    adults_add = (By.XPATH, "//div[@class='col o2']//button[contains(@class,'btn btn-white bootstrap-touchspin-up')]")
    adults_sub = (By.XPATH, "//div[@class='col o2']//button[contains(@class,'btn btn-white bootstrap-touchspin-down')]")
    kids_add = (By.XPATH, "//div[@class='col 01']//button[contains(@class,'btn btn-white bootstrap-touchspin-up')]")
    kids_sub = (By.XPATH, "//div[@class='col 01']//button[contains(@class,'btn btn-white bootstrap-touchspin-down')]")
    search_btn = (By.XPATH, "//div[@class='col-md-2 col-xs-12 o1']//button[@class='btn btn-primary btn-block']")


class SearchFlightsFormLocators:
    one_way_radio = (By.XPATH, "//label[text()='One Way']")
    round_trip_radio = (By.XPATH, "//label[text()='Round Trip']")
    cabinclass_select = (By.XPATH, "//select[@name='cabinclass']")
    first_class = (By.XPATH, "//li[text()='First']")
    economy_class = (By.XPATH, "//li[text()='Economy']")
    business_class = (By.XPATH, "//li[text()='Business']")
    loc_from_inactive = (By.XPATH, "//div[@id='s2id_location_from']")
    loc_from_active = (By.XPATH, "//div[@id='select2-drop']//input[@class='select2-input']")
    flight_date_start = (By.XPATH, "//input[@id='FlightsDateStart']")
    adults_input_value = (By.XPATH, "//input[@name='fadults']")
    adults_add = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-up '])[3]")
    adults_sub = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-down '])[3]")
    kids_input_value = (By.XPATH, "//input[@name='fchildren']")
    kids_add = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-up '])[4]")
    kids_sub = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-down '])[4]")
    infants_input_value = (By.XPATH, "//input[@name='finfant']")
    infants_add = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-up '])[5]")
    infants_sub = (By.XPATH, "(//button[@class='btn btn-white bootstrap-touchspin-down '])[5]")
    search_btn = (By.XPATH, "//div[@class='col-xs-12 col-md-1']//button[@class='btn-primary btn btn-block']")


class SearchTabsLocators:
    hotels_tab = (By.XPATH, "//a[@data-name='hotels']")
    flights_tab = (By.XPATH, "//a[@data-name='flights']")
    tours_tab = (By.XPATH, "//a[@data-name='tours']")
    transfer_tab = (By.XPATH, "//a[@data-name='transfer']")
    visa_tab = (By.XPATH, "//a[@data-name='visa']")


class SearchResultsLocators:
    search_title = (By.XPATH, "//span[@class='text-primary']")
    change_search_btn = (By.XPATH, "//button[@data-target='#change-search']")


class UserAccountLocators:
    welcome_msg = (By.XPATH, "//h3[@class='text-align-left']")
    bookings_tab = (By.LINK_TEXT, "Bookings")
    my_profile_tab = (By.LINK_TEXT, "My profile")
    wishlist_tab = (By.LINK_TEXT, "Wishlist")
    newsletter_tab = (By.LINK_TEXT, "Newsletter")
