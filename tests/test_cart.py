
from playwright.sync_api import Page, expect


def test_add_product_to_cart(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    cart_badge = logged_in_page.locator(
        '[data-test="shopping-cart-badge"]'
    )
    expect(cart_badge).to_have_text("1")

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    expect(
        logged_in_page.locator(
            '[data-test="cart-list"] [data-test="inventory-item-name"]'
        )
    ).to_have_text("Sauce Labs Backpack")


def test_remove_product_from_cart(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    logged_in_page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    expect(
        logged_in_page.locator('[data-test="inventory-item"]')
    ).to_have_count(0)

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_count(0)


def test_add_multiple_products_to_cart(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ).click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("2")

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    cart_items = logged_in_page.locator(
        '[data-test="cart-list"] [data-test="inventory-item"]'
    )
    expect(cart_items).to_have_count(2)


def test_remove_one_product_keeps_other_product_in_cart(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    logged_in_page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    cart_items = logged_in_page.locator(
        '[data-test="cart-list"] [data-test="inventory-item"]'
    )

    expect(cart_items).to_have_count(1)
    expect(
        cart_items.locator('[data-test="inventory-item-name"]')
    ).to_have_text("Sauce Labs Bike Light")
    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")


def test_cart_persists_when_navigating_back_to_inventory(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    expect(
        logged_in_page.locator('[data-test="cart-list"] [data-test="inventory-item"]')
    ).to_have_count(1)

    logged_in_page.locator('[data-test="continue-shopping"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")

    expect(
        logged_in_page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
    ).to_be_visible()


def test_cart_remains_empty_after_removing_all_products(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()

    logged_in_page.locator(
        '[data-test="remove-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="remove-sauce-labs-bike-light"]'
    ).click()

    expect(
        logged_in_page.locator(
            '[data-test="cart-list"] [data-test="inventory-item"]'
        )
    ).to_have_count(0)

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_count(0)

    logged_in_page.locator('[data-test="continue-shopping"]').click()

    expect(
        logged_in_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
    ).to_be_visible()
