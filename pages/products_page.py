
from playwright.sync_api import expect


class ProductsPage:

    def __init__(self, page):
        self.page = page

        # Products page elements
        self.page_title = page.locator(".title")
        self.products = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")

    # Verify products page heading
    def verify_page_heading(self):
        expect(self.page_title).to_have_text("Products")

    # Verify number of products
    def verify_product_count(self, count):
        expect(self.products).to_have_count(count)

    # Verify product name
    def verify_product_name(self, name):
        expect(self.product_names.first).to_have_text(name)

    # Verify product price
    def verify_product_price(self, price):
        expect(self.product_prices.first).to_have_text(price)
