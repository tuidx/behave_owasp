import allure
from behave.model_core import Status
from selenium import webdriver
import platform


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-prompt-on-repost')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--start-maximized')
    options.add_argument('--incognito-mode')
    options.add_argument('--disable-cache')
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    if platform.system() == 'Linux':
        context.browser = webdriver.Chrome(options=options)
    elif platform.system() == 'Windows':
        context.browser = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe", options=options)


def after_scenario(context, scenario):
    if scenario.status == Status.failed:
        allure.attach(context.browser.get_screenshot_as_png(), 'failed.png', 'image/png')
        context.browser.quit()

