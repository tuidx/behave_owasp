from behave import *
from zapv2 import ZAPv2
import subprocess
import time
import allure
from pages.login_page import LoginPage


@Given("The testpage page is loaded")
def step_impl(context):
    page = LoginPage(context)
    page.visit(context)
    page.wait_page_loaded()


@when('the user enter login "{login}" and password "{password}"')
def step_impl(context, login, password):
    page = LoginPage(context)
    page.input_user(login)
    page.input_password(password)


@when('the user click login')
def step_impl(context):
    page = LoginPage(context)
    page.click_login()


@step(u"the user do a scanner")
def step_impl(context):
    subprocess.Popen('./owasp.sh')
    time.sleep(5)
    target = context.browser.current_url
    apikey = '6ojksn3a4nnepjm4ju03hh7rio'
    zap = ZAPv2(apikey=apikey, proxies={'http': 'http://127.0.0.1:8089', 'https': 'https://127.0.0.1:8089'})
    print('zap has started')
    time.sleep(2)
    scanid = zap.spider.scan(target)
    time.sleep(2)
    while int(zap.spider.status(scanid)) < 100:
        time.sleep(2)

    while int(zap.pscan.records_to_scan) > 0:
        time.sleep(2)

    scanid = zap.ascan.scan(target)
    while int(zap.ascan.status(scanid)) < 100:
        time.sleep(5)

    allure.attach(zap.core.htmlreport(apikey=apikey), name="Security report",
                  attachment_type=allure.attachment_type.HTML, extension='html')
    assert len(zap.core.alerts()) == 0, 'Security bugs has been found'
    zap.core.shutdown()
    time.sleep(2)
