
from playwright.sync_api import expect


class CartPage:

    def __init__(self, page):
        self.page = page

        # Cart page elements
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_items = page.locator(".cart_item")
        self.remove_backpack_button = page.locator(
            "#remove-sauce-labs-backpack"
        )

    # Add Backpack to cart
    def add_backpack(self):
        self.page.locator(
            "#add-to-cart-sauce-labs-backpack"
        ).click()

    # Add Bike Light to cart
    def add_bike_light(self):
        self.page.locator(
            "#add-to-cart-sauce-labs-bike-light"
        ).click()

    # Verify cart badge count
    def verify_cart_count(self, count):
        expect(self.cart_badge).to_have_text(str(count))

    # Open cart
    def open_cart(self):
        self.cart_icon.click()

    # Verify number of cart items
    def verify_cart_items(self, count):
        expect(self.cart_items).to_have_count(count)

    # Verify product name in cart
    def verify_product_name(self, name):
        expect(
            self.page.locator(".inventory_item_name")
        ).to_have_text(name)

    # Remove Backpack
    def remove_backpack(self):
        self.remove_backpack_button.click()

    # Verify cart badge is empty
    def verify_cart_badge_empty(self):
        expect(self.cart_badge).to_have_count(0)
