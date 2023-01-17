import time
import model
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from model.pages import practice_form
from model.pages.practice_form import PracticeForm
from model.data.student import Student
import allure
from allure_commons.types import Severity
from model.utils import attach


form = PracticeForm()


@allure.title('Successful registration')
@allure.tag('user', 'ui', 'A.Chizh')
@allure.severity(Severity.CRITICAL)
@allure.id('1')
def test_form_filling():
    andrew = Student(
        first_name='Andrew',
        last_name='Chizh',
        email='andrechizh.ru@yandex.ru',
        phone_number='8918334613',
        address='Krasnodar',
        birthday='08 December,1992',
        gender='Male',
        hobby='Reading',
        subject='Arts',
        picture='picture.png',
        state='Uttar Pradesh',
        city='Merrut'
    )
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    
    browser.config.driver = driver

    with allure.step('Open page'):
        form.open()
    with allure.step('Fill form'):
        form.filling(andrew).click_submit()
    with allure.step('Assert info'):
        form.assert_information(andrew)
        time.sleep(1)
    attach.add_video(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()


