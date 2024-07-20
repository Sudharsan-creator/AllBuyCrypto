
import pytest

from ABC_pages.login_page import login_page
from ABC_utility.test_data import test_data
from conftest import user_name
from conftest import pass_word


@pytest.mark.usefixtures("init_driver")
class Test_login:

    def test_valid_credentials(self):
        Login_page = login_page(self.driver)
        Login_page.set_email_address(test_data.user_name)
        Login_page.set_password_field(test_data.pass_word)
        Login_page.click_submit_button()
