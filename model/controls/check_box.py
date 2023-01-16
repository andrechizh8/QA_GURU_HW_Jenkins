import selene
from selene.support.shared import browser
from selene import be,have

class Checkboxes:
    def __init__(self, element: selene.Element):
        self.element = element

    def set_checkbox(self, value):
        self.element.element_by(have.text(value)).click()
        return self