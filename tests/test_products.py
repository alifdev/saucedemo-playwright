
from playwright.sync_api import Page, expect


def test_inventory_displays_six_products(logged_in_page: Page):
    products = logged_in_page.locator('[data-test="inventory-item"]')

    expect(products).to_have_count(6)


def test_products_can_be_sorted_by_price_low_to_high(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="product-sort-container"]'
    ).select_option("lohi")

    price_elements = logged_in_page.locator(
        '[data-test="inventory-item-price"]'
    )

    prices = [
        float(price.replace("$", ""))
        for price in price_elements.all_text_contents()
    ]

    assert prices == sorted(prices), (
        f"Products are not sorted from lowest to highest price: {prices}"
    )


def test_user_can_open_product_details(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="item-4-title-link"]'
    ).click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/inventory-item.html?id=4"
    )

    expect(
    logged_in_page.locator(".inventory_details_name")
    ).to_have_text("Sauce Labs Backpack")

    expect(
        logged_in_page.locator('[data-test="inventory-item-price"]')
    ).to_have_text("$29.99")

    expect(
        logged_in_page.locator('[data-test="add-to-cart"]')
    ).to_be_visible()


def test_add_product_to_cart_from_details(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="item-4-title-link"]'
    ).click()

    expect(
        logged_in_page.locator(".inventory_details_name")
    ).to_have_text("Sauce Labs Backpack")

    logged_in_page.locator('[data-test="add-to-cart"]').click()

    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")

    expect(
        logged_in_page.locator('[data-test="remove"]')
    ).to_be_visible()


def test_products_can_be_sorted_by_price_high_to_low(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="product-sort-container"]'
    ).select_option("hilo")

    price_elements = logged_in_page.locator(
        '[data-test="inventory-item-price"]'
    )

    prices = [
        float(price.replace("$", ""))
        for price in price_elements.all_text_contents()
    ]

    assert prices == sorted(prices, reverse=True)


def test_products_can_be_sorted_by_name_a_to_z(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="product-sort-container"]'
    ).select_option("az")

    names = logged_in_page.locator(
        '[data-test="inventory-item-name"]'
    ).all_text_contents()

    assert names == sorted(names)


def test_products_can_be_sorted_by_name_z_to_a(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="product-sort-container"]'
    ).select_option("za")

    names = logged_in_page.locator(
        '[data-test="inventory-item-name"]'
    ).all_text_contents()

    assert names == sorted(names, reverse=True)
