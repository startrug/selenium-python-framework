class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.open()
