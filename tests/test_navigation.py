
from playwright.sync_api import Page, expect


def test_user_can_logout(logged_in_page: Page):
    logged_in_page.locator("#react-burger-menu-btn").click()

    logged_in_page.locator("#logout_sidebar_link").click()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/")
    expect(
        logged_in_page.locator('[data-test="login-button"]')
    ).to_be_visible()


def test_remove_product_from_inventory(logged_in_page: Page):
    add_button = logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    )
    remove_button = logged_in_page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    )

    add_button.click()
    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")

    remove_button.click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_count(0)
    expect(add_button).to_be_visible()



def test_empty_cart_has_no_items(logged_in_page: Page):
    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    expect(
        logged_in_page.locator(
            '[data-test="cart-list"] [data-test="inventory-item"]'
        )
    ).to_have_count(0)

    expect(
        logged_in_page.locator('[data-test="checkout"]')
    ).to_be_visible()


def test_sidebar_menu_can_open_and_close(logged_in_page: Page):
    menu_button = logged_in_page.locator("#react-burger-menu-btn")
    close_button = logged_in_page.locator("#react-burger-cross-btn")
    sidebar = logged_in_page.locator(".bm-menu")

    menu_button.click()
    expect(sidebar).to_be_visible()
    expect(
        logged_in_page.locator("#logout_sidebar_link")
    ).to_be_visible()

    close_button.click()
    expect(sidebar).not_to_be_visible()


def test_about_menu_navigation(logged_in_page: Page):
    logged_in_page.locator("#react-burger-menu-btn").click()

    logged_in_page.locator("#about_sidebar_link").click()

    expect(logged_in_page).to_have_url(
        "https://saucelabs.com/"
    )


def test_logout_clears_authenticated_session(logged_in_page: Page):
    logged_in_page.locator("#react-burger-menu-btn").click()
    logged_in_page.locator("#logout_sidebar_link").click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/"
    )

    logged_in_page.goto("https://www.saucedemo.com/inventory.html")

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/"
    )
    expect(
        logged_in_page.locator('[data-test="login-button"]')
    ).to_be_visible()
