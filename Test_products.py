
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


# Test 1: Verify products page heading
def test_products_page_heading(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.verify_page_heading()


# Test 2: Verify products are displayed
def test_products_are_visible(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.verify_product_count(6)


# Test 3: Verify product name
def test_product_name(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.verify_product_name("Sauce Labs Backpack")


# Test 4: Verify product price
def test_product_price(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.verify_product_price("$29.99")
