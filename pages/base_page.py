class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self, config):
        self.driver.get(config["tested_page"])
