
from playwright.sync_api import expect


class CheckoutPage:

    def __init__(self, page):
        self.page = page

        # Checkout information fields
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator("[data-test='error']")

        # Order summary elements
        self.product_name = page.locator(".inventory_item_name")
        self.product_price = page.locator(".inventory_item_price")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.total = page.locator(".summary_total_label")

        # Finish order elements
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    # Enter customer information
    def enter_customer_information(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    # Continue to order summary
    def continue_checkout(self):
        self.continue_button.click()

    # Verify checkout error
    def verify_error(self, message):
        expect(self.error_message).to_contain_text(message)

    # Verify product name
    def verify_product_name(self, name):
        expect(self.product_name).to_have_text(name)

    # Verify product price
    def verify_product_price(self, price):
        expect(self.product_price).to_have_text(price)

    # Verify subtotal
    def verify_subtotal(self, amount):
        expect(self.subtotal).to_have_text(
            f"Item total: {amount}"
        )

    # Verify total
    def verify_total(self, amount):
        expect(self.total).to_have_text(
            f"Total: {amount}"
        )

    # Finish order
    def finish_order(self):
        self.finish_button.click()

    # Verify successful order
    def verify_order_success(self):
        expect(self.success_message).to_have_text(
            "Thank you for your order!"
        )
