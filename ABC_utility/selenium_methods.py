from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Selenium_helper:
    def __init__(self, driver):
        self.driver = driver

    def web_element_enter(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def web_element_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()

    def only_locator(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).click()
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).send_keys("BTC")
