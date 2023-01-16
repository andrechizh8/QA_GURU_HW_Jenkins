import time

import model
from selene.support.shared import browser
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

    with allure.step('Open page'):
        form.open()
    with allure.step('Fill form'):
        form.filling(andrew).click_submit()
    with allure.step('Assert info'):
        form.assert_information(andrew)
        time.sleep(1)
    # attach.add_html(browser)
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_video(browser)
    # browser.quit()


