
from pages.login_page import LoginPage
from pages.cart_page import CartPage


# Test 1: Add product and verify cart badge
def test_add_product_to_cart(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_backpack()
    cart.verify_cart_count(1)


# Test 2: Verify product name inside cart
def test_verify_product_in_cart(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_backpack()
    cart.open_cart()

    cart.verify_cart_items(1)
    cart.verify_product_name("Sauce Labs Backpack")


# Test 3: Remove product from cart
def test_remove_product_from_cart(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_backpack()
    cart.open_cart()
    cart.remove_backpack()

    cart.verify_cart_items(0)
    cart.verify_cart_badge_empty()


# Test 4: Add multiple products
def test_add_multiple_products(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(page)
    cart.add_backpack()
    cart.add_bike_light()

    cart.verify_cart_count(2)
    cart.open_cart()
    cart.verify_cart_items(2)
