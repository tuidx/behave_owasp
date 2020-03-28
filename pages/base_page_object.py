from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, browser, base_url=''):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def wait_clickable(self, locator):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(locator), "Element not found to be clickable")


