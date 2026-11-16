
from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

        # Login page elements
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    # Open website
    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    # Enter username and password
    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    # Click login button
    def click_login(self):
        self.login_button.click()

    # Complete login process
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Verify successful login
    def verify_successful_login(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

    # Verify login error
    def verify_error(self, expected_message):
        expect(self.error_message).to_contain_text(
            expected_message
        )
