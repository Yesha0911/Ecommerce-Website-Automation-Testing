
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Reusable function to open checkout
def open_checkout(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_backpack()
    cart.open_cart()

    page.locator("#checkout").click()


# Test 1: Verify checkout page opens
def test_checkout_page_opens(page):

    open_checkout(page)

    checkout = CheckoutPage(page)

    assert page.url.endswith("checkout-step-one.html")

    assert checkout.first_name.is_visible()
    assert checkout.last_name.is_visible()
    assert checkout.postal_code.is_visible()


# Test 2: Verify customer information
def test_customer_information(page):

    open_checkout(page)

    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        "Yesha", "Shah", "380001"
    )

    checkout.continue_checkout()

    assert page.url.endswith("checkout-step-two.html")


# Test 3: Verify error for missing information
def test_checkout_with_missing_information(page):

    open_checkout(page)

    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        "", "Shah", "380001"
    )

    checkout.continue_checkout()

    checkout.verify_error("First Name is required")


# Test 4: Verify order summary and price
def test_order_summary(page):

    open_checkout(page)

    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        "Yesha", "Shah", "380001"
    )

    checkout.continue_checkout()

    checkout.verify_product_name("Sauce Labs Backpack")
    checkout.verify_product_price("$29.99")
    checkout.verify_subtotal("$29.99")
    checkout.verify_total("$32.39")


# Test 5: Verify successful order completion
def test_finish_order(page):

    open_checkout(page)

    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        "Yesha", "Shah", "380001"
    )

    checkout.continue_checkout()
    checkout.finish_order()

    checkout.verify_order_success()
