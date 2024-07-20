# In this code i wanna show you how to trade on spot trade page ;
import time

import pytest

from ABC_pages.Spottrade_page import spotrade_page
from ABC_pages.login_page import login_page
from ABC_utility.test_data import test_data


@pytest.mark.usefixtures("init_driver")
class Test_spot_trade:

    def test_spot_trade_page(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
        time.sleep(2)

# This is spot code
        spot_trade = spotrade_page(self.driver)
        spot_trade.navigate_spot_page()
        time.sleep(2)

        self.driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)

        spot_trade.place_limit(test_data.Spot_Limit_Price)
        spot_trade.click_limit_btn()
        time.sleep(1)
        spot_trade.click_confirmation_btn01()

