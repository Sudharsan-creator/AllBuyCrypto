import time

from selenium.webdriver.common.by import By

from ABC_utility.selenium_methods import Selenium_helper


class OTC_page(Selenium_helper):
    OTC_trade_page = (By.XPATH, "//a[contains(text(),'OTC')]")
    From_currency = (By.XPATH, "//button[text()=' BTC ']")
    BNB = (By.XPATH, "//div[text()=' BNB ']")
    To_Currency = (By.XPATH, "//button[text()=' ETH ']")
    BTC = (By.XPATH, "//div[text()=' BTC ']")
    from_amount_textbox = (By.NAME, "quantityone")
    quote_button = (By.XPATH, "//div[text()='Request for Quote']")
    OTC_Accept_quote = (By.XPATH, "//button[text()='Accept Quote']")
    Quote_close_btn = (By.CLASS_NAME, 'mat-mdc-button-touch-target')

    Limit_order_otc = (By.XPATH, "//span[text()='Limit']")
    Limit_from_amount = (By.XPATH, "(//input[@placeholder='0.00000000'])[1]")
    Limit_Submit_Quote = (By.XPATH, "//div[contains(@class,'btn request_btn')]")
    Limit_quote_confirmation_btn = (By.XPATH, "//button[contains(@class,'btn accept-quote-btn')]")
    Limit_Close_btn = (By.CLASS_NAME, 'mat-mdc-button-touch-target')
    OTC_History_Xpath = (By.XPATH, "//div[text()='OTC Trading History ']")

    Arrow_up = (By.XPATH,"//mat-icon[text()='keyboard_arrow_up']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_OTC_page(self):
        self.only_locator(self.OTC_trade_page)
        time.sleep(2)

    def OTC_from_coin(self):
        self.only_locator(self.From_currency)

    def select_coin01(self):
        self.only_locator(self.BNB)

    def OTC_To_coin(self):
        self.only_locator(self.To_Currency)

    def select_coin02(self):
        self.only_locator(self.BTC)

    def enter_from_amount(self, value):
        self.web_element_enter(self.from_amount_textbox, value)

    def click_quote_btn(self):
        self.only_locator(self.quote_button)

    def OTC_Confirmation(self):
        self.only_locator(self.OTC_Accept_quote)

    def OTC_trade_close(self):
        self.only_locator(self.Quote_close_btn)

    # In this section reflects the how-to works the limit order OTC field
    def Limit_Order_OTC(self):
        self.only_locator(self.Limit_order_otc)

    def Limit_amount_textbox(self, value):
        self.web_element_enter(self.Limit_from_amount, value)

    def Limit_Quote_submit(self):
        self.only_locator(self.Limit_Submit_Quote)

    def Limit_Quote_confirmation(self):
        self.only_locator(self.Limit_quote_confirmation_btn)

    def Limit_Close_Btn(self):
        self.only_locator(self.Limit_Close_btn)

    def Arrow_up_btn(self):
        self.only_locator(self.Arrow_up)

    # In this code is represent the OTC history panel
    def OTC_history_panel(self):
        self.only_locator(self.OTC_History_Xpath)
