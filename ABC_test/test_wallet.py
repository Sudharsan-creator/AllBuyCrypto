import time

import pytest
from selenium import webdriver
from ABC_pages.login_page import login_page
from ABC_pages.wallet_page import wallet_page
from ABC_utility.test_data import test_data


@pytest.mark.usefixtures("init_driver")
class Test_wallet:
    def test_wallet_navigation(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
        time.sleep(2)

        # Asset Page Scripts
        asset_page = wallet_page(self.driver)
        asset_page.navigate_wallet_page()
        time.sleep(2)

        # Select crypto asset
        asset_page.select_crypto_cart()








