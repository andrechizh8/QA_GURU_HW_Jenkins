import pytest
from selene.support.shared import browser
from model.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://demoqa.com/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
