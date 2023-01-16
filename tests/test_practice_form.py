import model
from model.pages import practice_form
from model.pages.practice_form import PracticeForm
from model.data.student import Student

form = PracticeForm()


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
    form.open()
    form.filling(andrew).click_submit()
    form.assert_information(andrew).click_close_button()
