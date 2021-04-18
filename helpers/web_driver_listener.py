import logging
import datetime
from selenium.webdriver.support.events import AbstractEventListener

log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    filename=rf"C:\Users\DELL\Code\selenium_logs\{log_filename}.log",
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO
)


class WebDriverListener(AbstractEventListener):
    def __init__(self):
        self.logger = logging.getLogger("selenium")
        self.logger.setLevel(logging.INFO)

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigated to {url}")

    def before_find(self, by, value, driver):
        self.logger.info(f"Finding element by {by} {value}")

    def after_find(self,by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        self.logger.info(f"{element.get_attribute('text')} clicked")

    # def __init__(self, driver):
    #     self.browser = driver
    #     self.driver = EventFiringWebDriver(self.browser, WebDriverListener())
    #     self.logger = L.getLogger("logger")
    #     self.navigating += self.web_driver_listener_navigating
    #     self.navigated += self.web_driver_listener_navigated
    #     self.finding_element += self.web_driver_listener_finding_element
    #     self.element_clicking += self.web_driver_listener_element_clicking
    #     self.element_clicked += self.web_driver_listener_element_clicked
    #     self.element_value_changed += self.web_driver_listener_element_value_changed
    #
    # def web_driver_listener_navigating(self, sender, event_arg):
    #     L.log(f"Navigating to {event_arg.Url}")
    #
    # def web_driver_listener_navigated(self, sender, event_arg):
    #     self.log_screenshot(f"Navigated to [{event_arg.Driver.Title}]({event_arg.Url})")
    #
    # def web_driver_listener_finding_element(self, sender, event_arg):
    #     self.log_message(f"Finding element `{event_arg.FindMethod}`")
    #
    # def web_driver_listener_element_clicking(self, sender, event_arg):
    #     self.log_message(f"Clicking on the {event_arg.Element.TagName} `{event_arg.Element.Text}` {event_arg.Element}")
    #
    # def web_driver_listener_element_clicked(self, sender, event_arg):
    #     self.log_screenshot(f"{event_arg.Element} clicked")
    #
    # def web_driver_listener_element_value_changed(self, sender, event_arg):
    #     self.log_screenshot(f"Value of the {event_arg.Element} changed to `{event_arg.Value}`")
    #
    # def log_message(self, text):
    #     self.logger.info(text)
    #
    # def log_screenshot(self, file_name):
    #     SE.take_standard_screenshot(file_name)
