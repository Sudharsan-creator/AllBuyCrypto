# In this code i want to shows you how to use the history page
import time

import pytest

from ABC_pages.History_page import History_page
from ABC_pages.login_page import login_page
from ABC_utility.test_data import test_data


@pytest.mark.usefixtures("init_driver")
class Test_history_page:
    def test_history_page(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
        time.sleep(2)

# in this section is starts history page auto script
        HP = History_page(self.driver)
        HP.Navigation_history_page()
        time.sleep(1)
        HP.Navigation_deposit()
        time.sleep(1)
        HP.Navigation_Withdrawal()
        time.sleep(1)
        HP.Navigation_NFT()
        time.sleep(1)
        HP.Navigation_Repay()
        time.sleep(1)
        HP.Navigation_Credits()
        time.sleep(2)

        HP.Choose_coin()
        time.sleep(1)
        HP.Choose_coin_name()
        time.sleep(1)

        HP.Click_Calendar()
        time.sleep(1)

