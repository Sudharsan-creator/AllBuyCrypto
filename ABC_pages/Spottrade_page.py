# In this video i wanna show you for how to trade on Spot page
from selenium.webdriver.common.by import By

from ABC_utility.selenium_methods import Selenium_helper


class spotrade_page(Selenium_helper):
    Spot_page_link = (By.XPATH, "//a[contains(text(),'Spot')]")
    Market_order_type = (By.XPATH, "//h5[text()='Market']")
    Market_order_quantiry_txt_box = (By.XPATH, "(//input[@name='fname'])[4]")
    Market_buy_btn = (By.XPATH, "(//button[contains(@class,'btn btn-primary')]//a)[3]")
    Market_confirmation_yes = (By.XPATH, "//button[text()='Yes']")
    Market_sell_order_txt_box = (By.XPATH, "(//input[@name='fname'])[6]")
    Market_sell_order_submit_btn = (By.XPATH, "(//button[.='Sell'])[2]")

    Stop_Limit_type_link = (By.XPATH, "//h5[text()='Stop Limit']")
    Stop_limit_condition_amt_txtbox = (By.XPATH, "(//input[@name='fname'])[7]")
    Stop_limit_limit_amt_txt_box = (By.XPATH, "(//input[@name='fname'])[8]")
    Stop_Limit_Buy_Btn = (By.XPATH, "(//button[.='Buy'])[3]")
    Stop_Buy_COnfirmation_Btn = (By.XPATH, "//button[text()='Yes']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_spot_page(self):
        self.only_locator(self.Spot_page_link)

    #      self.driver.execute_script("windows,scrollBy(0,600);")
    def change_market_order(self):
        self.only_locator(self.Market_order_type)

    def Market_order_amount(self, amount):
        self.web_element_enter(self.Market_order_quantiry_txt_box, amount)

    def Market_click_buy_btn(self):
        self.only_locator(self.Market_buy_btn)

    def Market_Buy_confirmation(self):
        self.only_locator(self.Market_confirmation_yes)

    def Market_Sell_Order_Amount_Field(self, amount02):
        self.web_element_enter(self.Market_sell_order_txt_box, amount02)

    def Market_Sell_Order_Submit_Button(self):
        self.only_locator(self.Market_sell_order_submit_btn)

    def Market_Sell_confirmation(self):
        self.only_locator(self.Market_confirmation_yes)

    # The stop-limit order types starts here
    def Stop_limit_navigation(self):
        self.only_locator(self.Stop_Limit_type_link)

    def Stop_limit_condition_price(self, stop_limie_value):
        self.web_element_enter(self.Stop_limit_condition_amt_txtbox, stop_limie_value)

    def Stop_limit_price_txt_box(self, stop_limit_price_txt_box):
        self.web_element_enter(self.Stop_limit_limit_amt_txt_box, stop_limit_price_txt_box)

    def Stop_limit_buy_button(self):
        self.only_locator(self.Stop_Limit_Buy_Btn)

    def Stop_limit_confirmation_yes(self):
        self.only_locator(self.Stop_Buy_COnfirmation_Btn)
