import time

import pytest
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from model.utils import attach


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser.config.driver = driver

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
