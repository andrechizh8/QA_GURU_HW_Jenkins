from selene.support.shared import browser
from selene import be, have
from model.utils.file_path import path_to_file
from model.controls.check_box import Checkboxes
from model.controls.radio_button import RadioButtons
from model.controls.dropdown import DropdownButtons
from model.controls.datepicker import Datepicker


class PracticeForm:

    def open(self):
        browser.open("/automation-practice-form")
        # browser.driver.execute_script('document.querySelector(".body-height").style.transform = "scale(.6)"')
        return self

    def fill_name(self, student):
        browser.element('#firstName').should(be.blank).type(student.first_name)
        browser.element('#lastName').should(be.blank).type(student.last_name)
        return self

    def fill_email(self, student):
        browser.element('#userEmail').should(be.blank).type(student.email)
        return self

    def set_gender(self, student):
        RadioButtons(browser.all("[name='gender']")).set_radio(student.gender)
        return self

    def fill_phone_number(self, student):
        browser.element('#userNumber').should(be.blank).type(student.phone_number)
        return self

    def set_hobby(self, student):
        Checkboxes(browser.all("[for^='hobbies-checkbox']")).set_checkbox(student.hobby)
        return self

    def set_photo(self):
        path_to_file('#uploadPicture', 'resources/picture.png')
        return self

    def fill_address(self, student):
        browser.element('#currentAddress').should(be.blank).type(student.address)
        return self

    def set_date(self, student):
        birthday = Datepicker(browser.element('#dateOfBirthInput'))
        birthday.set_date(student.birthday)
        return self

    def set_subject(self, student):
        browser.element('#subjectsInput').type(student.subject).press_enter()
        return self

    def set_state(self, student):
        DropdownButtons(browser.element('#state')).select_dropdown(student.state)
        return self

    def set_city(self, student):
        DropdownButtons(browser.element('#city')).select_dropdown(student.city)
        return self

    def click_submit(self):
        browser.element('#submit').press_enter()
        return self

    def filling(self, student):
        self.fill_name(student) \
            .fill_email(student) \
            .set_gender(student) \
            .fill_phone_number(student) \
            .set_date(student) \
            .set_subject(student) \
            .set_hobby(student) \
            .set_photo() \
            .fill_address(student) \
            .set_state(student) \
            .set_city(student)
        return self

    def assert_information(self, student):
        browser.all('.table td:nth-child(2)').should(have.texts(
            student.first_name + ' ' + student.last_name,
            student.email,
            student.gender,
            student.phone_number,
            student.birthday,
            student.subject,
            student.hobby,
            student.picture,
            student.address,
            student.state + ' ' + student.city
        ))
        return self

    def click_close_button(self):
        browser.element('#closeLargeModal').click()
        return self
