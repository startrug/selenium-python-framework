from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from helpers.web_driver_listener import WebDriverListener
from msedge.selenium_tools import EdgeOptions, Edge


class DriverFactory:
    @staticmethod
    def get_driver(browser, headless_mode=False) -> EventFiringWebDriver:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if headless_mode is True:
                options.add_argument("--headless")
            driver = EventFiringWebDriver(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener()
            )
            return driver
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless_mode is True:
                options.headless = True
            driver = EventFiringWebDriver(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener()
            )
            return driver
        elif browser == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            if headless_mode is True:
                options.headless = True
            driver_path = EdgeChromiumDriverManager().install()
            driver = EventFiringWebDriver(
                Edge(executable_path=driver_path, options=options),
                WebDriverListener()
            )
            return driver
        raise Exception("Provide valid driver name")
