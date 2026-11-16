
# E-commerce Website Automation Testing

## Application
Website: https://www.saucedemo.com/

## Testing Tools
- Python
- Playwright
- Pytest
- Pytest HTML

## Test Cases

### 1. Login Module

| ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Login with valid credentials | User reaches Products page |
| TC02 | Login with invalid password | Error message is displayed |
| TC03 | Login with empty username | Username required error |
| TC04 | Login with empty password | Password required error |

### 2. Products Module

| ID | Test Scenario | Expected Result |
|---|---|---|
| TC05 | Verify Products page heading | Products heading is visible |
| TC06 | Verify product count | Six products are displayed |
| TC07 | Verify first product name | Sauce Labs Backpack |
| TC08 | Verify first product price | $29.99 |

### 3. Shopping Cart Module

| ID | Test Scenario | Expected Result |
|---|---|---|
| TC09 | Add product to cart | Cart badge shows 1 |
| TC10 | Verify product in cart | Backpack appears in cart |
| TC11 | Remove product | Cart becomes empty |
| TC12 | Add multiple products | Cart contains 2 products |

### 4. Checkout Module

| ID | Test Scenario | Expected Result |
|---|---|---|
| TC13 | Open checkout page | Customer fields are visible |
| TC14 | Enter customer information | User reaches order summary |
| TC15 | Submit missing information | Required field error appears |
| TC16 | Verify order summary | Correct product and price displayed |
| TC17 | Finish order | Order confirmation is displayed |

## Total Automated Test Cases
17
