import time

import pytest
from selenium.webdriver.common.by import By

from ABC_pages.OTC_page import OTC_page
from ABC_pages.login_page import login_page
from ABC_utility.test_data import test_data


@pytest.mark.usefixtures("init_driver")
class Test_OTC_page:
    def test_OTC_page(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
        time.sleep(2)

        otc = OTC_page(self.driver)
        otc.navigate_OTC_page()
        time.sleep(2)
        # Market Order OTC Trade section
        otc.OTC_from_coin()
        time.sleep(1)
        otc.select_coin01()
        time.sleep(1)
        otc.OTC_To_coin()
        time.sleep(1)
        otc.select_coin02()
        otc.enter_from_amount(test_data.OTC_value)
        otc.click_quote_btn()
        time.sleep(1)
        otc.OTC_Confirmation()
        time.sleep(1)
        otc.OTC_trade_close()
        time.sleep(2)

    # Limit Order OTC Trade
    def test_OTC_page02(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
        time.sleep(2)

        otc = OTC_page(self.driver)
        otc.navigate_OTC_page()
        time.sleep(2)

        otc.Limit_Order_OTC()
        time.sleep(1)
        otc.Limit_amount_textbox(test_data.Limit_OTC_value)
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)

        otc.Limit_Quote_submit()
        time.sleep(1)
        otc.Limit_Quote_confirmation()
        time.sleep(1)
        otc.Limit_Close_Btn()
        time.sleep(1)
        otc.Arrow_up_btn()
        time.sleep(2)
        otc.OTC_history_panel()
        time.sleep(1)
        self.driver.back()
