from pages.base_page_object import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    locator_dictionary = {
        "user": (By.ID, 'email'),
        "password": (By.ID, 'passwd'),
        "login": (By.ID, 'SubmitLogin')
    }

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='')

    def visit(self, context):
        context.browser.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
        time.sleep(3)

    def wait_page_loaded(self):
        self.wait_clickable(self.locator_dictionary["user"])

    def click_login(self):
        self.find_element(*self.locator_dictionary["login"]).click()

    def input_user(self, login):
        self.find_element(*self.locator_dictionary["user"]).send_keys(login)

    def input_password(self, password):
        self.find_element(*self.locator_dictionary["password"]).send_keys(password)
