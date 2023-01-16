import selene
from selene.support.shared import browser
from selene import be,have

class DropdownButtons:
    def __init__(self, element: selene.Element):
        self.element = element

    def select_dropdown(self, value):
        self.element.click()
        browser.all('[id^=react-select').element_by(have.exact_text(value)).click()
        return self