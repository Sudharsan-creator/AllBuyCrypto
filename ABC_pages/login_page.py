from selenium.webdriver.common.by import By

from ABC_utility.selenium_methods import Selenium_helper


class login_page(Selenium_helper):
    email_address_field = (By.ID, 'exampleInputEmail1')
    password_address_field = (By.ID, 'exampleInputEmail2')
    login_button = (By.XPATH, "//button[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_email_address(self, email):
        self.web_element_enter(self.email_address_field, email)

    def set_password_field(self, password):
        self.web_element_enter(self.password_address_field, password)

    def click_submit_button(self):
        self.web_element_click(self.login_button)





