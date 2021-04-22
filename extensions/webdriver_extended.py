from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class WebDriverExtended(EventFiringWebDriver):
    def __init__(self, driver, event_listener, config):
        super().__init__(driver, event_listener)
        self.base_url = config["base_url"]

    def open(self):
        self.get(self.base_url)