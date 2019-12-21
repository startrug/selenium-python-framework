# Test Automation Project

This is my first test automation project based on Selenium-Webdriver with Python. It's still developing package of automated tests of https://phptravels.net demo website.
The collection of tests contains:
- user login tests (correct / incorrect login and password)
- hotels search tests
- flights search tests
- tours search tests
- transfers search tests

## Project Features
- framework follows page object pattern
- data-driven tests - in most tests the option of loading data from an xlsx file has been implemented
- logger has been implemented in each step of test cases, e.g.
```
@allure.step("Setting destination to '{1}'")
    def set_destination(self, destination):
        self.logger.info(f"Setting destination: {destination}")
        self.driver.find_element(*SearchHotelsFormLocators.destination_inactive).click()
```
![Logs screenshot](https://raw.githubusercontent.com/startrug/phptravels-selenium-py/screenshots/logger.png "Logs screenshot")
- the ability to easily generate legible and attractive test reports using Allure (for more look "Generate Test Report" paragraph below)
- ...


## Getting Started

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

## Run Automated Tests

TODO

## Generate Test Report

To generate all tests report using Allure you need run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need use command:
```
$ allure serve <reports directory path>
```
![Allure report screenshot](https://raw.githubusercontent.com/startrug/phptravels-selenium-py/screenshots/allure_report.png "Allure report screenshot")
## License

TODO
