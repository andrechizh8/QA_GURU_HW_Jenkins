import selene
from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import Keys


class Datepicker:
    def __init__(self, element: selene.Element):
        self.element = element


    def set_date(self, value):
        self.element.send_keys(Keys.CONTROL, 'a').send_keys(value).press_enter()
        return self
