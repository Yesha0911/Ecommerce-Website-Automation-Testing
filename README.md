
# E-commerce Website Automation Testing

An end-to-end web application automation testing project built using Python, Playwright, and Pytest.

The project automates important e-commerce workflows on the SauceDemo demo application, including login, product validation, shopping cart operations, and checkout.

## Application Under Test

https://www.saucedemo.com/

## Technologies Used

- Python
- Playwright
- Pytest
- Pytest HTML

## Features

- Automated login testing
- Invalid and empty login validation
- Products page validation
- Product name, price, and count verification
- Add and remove products from cart
- Multiple product cart validation
- Checkout form validation
- Order summary and price verification
- Successful order completion
- Page Object Model (POM) design
- HTML test execution report
- Automatic screenshot capture when a test fails

## Test Coverage

| Module | Test Cases |
|---|---:|
| Login | 4 |
| Products | 4 |
| Shopping Cart | 4 |
| Checkout | 5 |
| **Total** | **17** |

## Project Structure

```text
Project-1-Ecommerce-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   ├── report.html
│   └── screenshots/
│
├── Test_login.py
├── Test_products.py
├── Test_cart.py
├── Test_checkout.py
├── conftest.py
├── test_cases.md
├── bug_report.md
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Yesha0911/Ecommerce-Website-Automation-Testing.git
```

### 2. Open the project folder

```bash
cd Project-1-Ecommerce-Automation
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Install Playwright Chromium

```bash
python -m playwright install chromium
```

## Execute Tests

Run all automated tests:

```bash
python -m pytest -v
```

Generate an HTML report:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

Open the HTML report on Windows:

```powershell
start reports/report.html
```

## Test Credentials

For the public SauceDemo demo application:

- Username: `standard_user`
- Password: `secret_sauce`

## Test Documentation

- `test_cases.md` — Test scenarios and expected results.
- `bug_report.md` — Bug reporting format and documented defect status.

## Design Pattern

The project follows the Page Object Model (POM), separating page locators and reusable actions from test scripts.

This improves code organization, readability, and maintainability.

## Disclaimer

This project is created for educational and portfolio purposes using a publicly available demo application.
