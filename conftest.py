
import pytest
from pathlib import Path
from playwright.sync_api import sync_playwright


# Browser fixture
@pytest.fixture
def page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()


# Capture test execution result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only if test fails
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:
            screenshot_folder = Path("reports/screenshots")
            screenshot_folder.mkdir(parents=True, exist_ok=True)

            test_name = item.name.replace("/", "_")
            screenshot_path = screenshot_folder / f"{test_name}.png"

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print(f"\nFailure screenshot saved: {screenshot_path}")
