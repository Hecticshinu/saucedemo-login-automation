import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():

    os.environ["DISPLAY"] = ":0"

    options = Options()

    options.binary_location = (
        "/data/data/com.termux/files/usr/bin/chromium-browser"
    )

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument(
        "--user-data-dir=/data/data/com.termux/files/usr/tmp/selenium-login"
    )

    service = Service(
        "/data/data/com.termux/files/usr/bin/chromedriver"
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    yield driver

    time.sleep(2)

    driver.quit()