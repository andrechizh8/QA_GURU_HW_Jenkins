import selene
from selene.support.shared import browser
from selene import be,have

class RadioButtons:

    def __init__(self, element: selene.Element):
        self.element = element

    def set_radio(self, value: str):
        self.element.element_by(have.value(value)).element('..').click()
        return self
