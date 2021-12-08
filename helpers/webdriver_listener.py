import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener


class WebDriverListener(AbstractEventListener):
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
    logging.basicConfig(
        # log file will be created in "tests" directory. Feel free to change the path or filename
        filename=f"{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )

    def __init__(self):
        self.logger = logging.getLogger("selenium")

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"{url} opened")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"{element.get_attribute('class')} clicked")
        else:
            self.logger.info(f"{element.get_attribute('text')} clicked")

    def before_change_value_of(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} value changed")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)
