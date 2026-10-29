
import re

from playwright.sync_api import Page, expect


def test_saucedemo_login_page(page: Page):
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title(re.compile("Swag Labs"))
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_login_with_valid_credentials(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url(re.compile(".*/inventory.html"))
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


def test_login_with_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text(
        "Username and password do not match"
    )


def test_login_with_empty_username(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Username is required")

def test_login_with_empty_password(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="login-button"]').click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Password is required")
