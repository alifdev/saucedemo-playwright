
import re
from datetime import datetime
from pathlib import Path

import pytest
from playwright.sync_api import Page


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    project_root = Path(__file__).resolve().parent.parent
    screenshot_dir = project_root / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    safe_test_name = re.sub(r"[^A-Za-z0-9_-]", "_", item.name)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    screenshot_path = (
        screenshot_dir / f"{safe_test_name}-{timestamp}.png"
    )

    try:
        page.screenshot(path=str(screenshot_path), full_page=True)
        print(f"\nFailure screenshot saved: {screenshot_path}")
    except Exception as error:
        print(f"\nCould not save failure screenshot: {error}")
