import time
from selenium.webdriver.common.by import By
from ABC_utility.selenium_methods import Selenium_helper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class wallet_page(Selenium_helper):
    Wallet_balance_page = (By.XPATH, "//a[contains(text(),'Wallet')]")
    Wallet_search = (By.NAME, 'search')
    BTC = (By.XPATH, "(//button[@id='btc-tab'])[1]")
    Copy_Address = (By.XPATH, "//button[text()='Copy']")
    Withdrawal_section = (By.ID, "nav-withdraw-tab")
    Unique_close = (By.CLASS_NAME, 'mat-mdc-button-touch-target')

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_wallet_page(self):
        self.only_locator(self.Wallet_balance_page)
        time.sleep(2)

    #def wallet_search_feature(self):
    # self.only_locator(self.Wallet_search).send_keys("BTC")
    # time.sleep(1)

    def select_crypto_cart(self):
        self.only_locator(self.BTC)
        time.sleep(1)
        self.only_locator(self.Copy_Address)
        print("Address Copied Successfully!")

        # Change to withdrawal section
        self.only_locator(self.Withdrawal_section)

        # Close the specific tab
        time.sleep(1)
        self.only_locator(self.Unique_close)
        time.sleep(1)
