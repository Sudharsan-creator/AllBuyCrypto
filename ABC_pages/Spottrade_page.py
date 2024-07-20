# In this video i wanna show you for how to trade on Spot page
from selenium.webdriver.common.by import By

from ABC_utility.selenium_methods import Selenium_helper


class spotrade_page(Selenium_helper):
    Spot_page_link = (By.XPATH, "//a[contains(text(),'Spot')]")
    Limit_price_textbox = (By.XPATH, "(//span[text()=' 0.00000000 BTC']/following::input)[1]")
    Limit_submit_btn = (By.XPATH, "(//button[contains(@class,'btn btn-primary')]//a)[1]")
    Limit_confirmation_btn = (By.XPATH, "//button[text()='Yes']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_spot_page(self):
        self.only_locator(self.Spot_page_link)

    #       self.driver.execute_script("windows,scrollBy(0,600);")

    def place_limit(self, value):
        self.web_element_enter(self.Limit_price_textbox, value)

    def click_limit_btn(self):
        self.only_locator(self.Limit_submit_btn)

    def click_confirmation_btn01(self):
        self.only_locator(self.Limit_confirmation_btn)
