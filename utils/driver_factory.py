from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from helpers.web_driver_listener import WebDriverListener


class DriverFactory:
    @staticmethod
    def get_driver(browser) -> EventFiringWebDriver:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = EventFiringWebDriver(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener()
            )
            return driver
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            driver = EventFiringWebDriver(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener()
            )
            return driver
        raise Exception("Provide valid driver name")
