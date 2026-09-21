import time

from pages.login_page import LoginPage


VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_valid_login(driver):

    page = LoginPage(driver)

    page.open()
    time.sleep(2)

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )
    time.sleep(2)

    assert "inventory" in driver.current_url

    time.sleep(2)
    
def test_blank_login(driver):

    page = LoginPage(driver)

    page.open()
    time.sleep(2)

    page.click_login()
    time.sleep(2)

    assert "Username is required" in page.get_error_message()

    time.sleep(2)


def test_valid_login_and_logout(driver):

    page = LoginPage(driver)

    page.open()
    time.sleep(2)

    page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )
    time.sleep(2)

    assert "inventory" in driver.current_url

    page.logout()
    time.sleep(2)

    assert driver.current_url == "https://www.saucedemo.com/"

    time.sleep(2)
