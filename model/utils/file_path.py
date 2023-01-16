import os
from selene.support.shared import browser
import tests

def path_to_file(selector,path):
    browser.element(selector).send_keys(
        os.path.abspath(os.path.join(os.path.dirname(tests.__file__),path)))