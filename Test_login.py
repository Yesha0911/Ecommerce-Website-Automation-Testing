
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


# Test 1: Successful login
def test_valid_login(page):

    login = LoginPage(page)

    login.open()
    login.login("standard_user", "secret_sauce")

    login.verify_successful_login()


# Test 2: Invalid password
def test_invalid_login(page):

    login = LoginPage(page)

    login.open()
    login.login("standard_user", "wrong_password")

    login.verify_error(
        "Username and password do not match"
    )


# Test 3 and 4: Empty login fields
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required")
    ]
)
def test_empty_login_fields(page, username, password, expected_error):

    login = LoginPage(page)

    login.open()
    login.login(username, password)

    login.verify_error(expected_error)
