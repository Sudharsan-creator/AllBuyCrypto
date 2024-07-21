# In this code i wanna shows you how to handle the history page
import time

from selenium.webdriver.common.by import By

from ABC_utility.selenium_methods import Selenium_helper


class History_page(Selenium_helper):
    History_page_URL = (By.XPATH, "//a[contains(text(),'History')]")
    Deposit_history_url = (By.ID, 'pills-deposite-tab')
    Withdrawal_history_url = (By.ID, 'pills-withdraw-tab')
    NFT_history_url = (By.ID, 'pills-nftrans-tab')
    NFT_repay_url = (By.ID, 'pills-nftrepay-tab')
    Credits_url = (By.ID, 'pills-virtual-tab')
    Choose_coin_dropdowm = (By.ID, 'mat-select-value-11')
    Select_particular_coin = (By.ID, 'mat-option-41')
    Click_calendar = (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[14]")
    Calendar_start_date = (By.XPATH, "//span[text()=' 2 ']")
    Calendar_end_date = (By.XPATH, "//span[text()=' 4 ']")
    Search_option = (By.XPATH, "(//button[.='Search'])[4]")
    Clear_option = (By.XPATH, "(//button[.='Clear'])[6]")

    def __init__(self, driver):
        super().__init__(driver)

    def Navigation_history_page(self):
        self.only_locator(self.History_page_URL)

    def Navigation_deposit(self):
        self.only_locator(self.Deposit_history_url)

    def Navigation_Withdrawal(self):
        self.only_locator(self.Withdrawal_history_url)

    def Navigation_NFT(self):
        self.only_locator(self.NFT_history_url)

    def Navigation_Repay(self):
        self.only_locator(self.NFT_repay_url)

    def Navigation_Credits(self):
        self.only_locator(self.Credits_url)

    def Choose_coin(self):
        self.only_locator(self.Choose_coin_dropdowm)

    def Choose_coin_name(self):
        self.only_locator(self.Select_particular_coin)

    def Click_Calendar(self):
        self.only_locator(self.Click_calendar)
        self.only_locator(self.Calendar_start_date)
        self.only_locator(self.Calendar_end_date)
        self.only_locator(self.Search_option)
        time.sleep(1)
        self.only_locator(self.Clear_option)
