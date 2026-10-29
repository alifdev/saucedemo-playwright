
from playwright.sync_api import Page, expect


def test_checkout_successful(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()
    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="firstName"]').fill("Alif")
    logged_in_page.locator('[data-test="lastName"]').fill("QA")
    logged_in_page.locator('[data-test="postalCode"]').fill("15143")
    logged_in_page.locator('[data-test="continue"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )

    expect(
        logged_in_page.locator('[data-test="inventory-item-name"]')
    ).to_have_text("Sauce Labs Backpack")

    logged_in_page.locator('[data-test="finish"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )

    expect(
        logged_in_page.locator('[data-test="complete-header"]')
    ).to_have_text("Thank you for your order!")


def test_checkout_rejects_empty_first_name(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()
    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="lastName"]').fill("QA")
    logged_in_page.locator('[data-test="postalCode"]').fill("15143")
    logged_in_page.locator('[data-test="continue"]').click()

    expect(
        logged_in_page.locator('[data-test="error"]')
    ).to_contain_text("First Name is required")


def test_checkout_rejects_empty_postal_code(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()
    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="firstName"]').fill("Alif")
    logged_in_page.locator('[data-test="lastName"]').fill("QA")
    logged_in_page.locator('[data-test="continue"]').click()

    expect(
        logged_in_page.locator('[data-test="error"]')
    ).to_contain_text("Postal Code is required")


def test_checkout_order_summary_and_total(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-bike-light"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="firstName"]').fill("Alif")
    logged_in_page.locator('[data-test="lastName"]').fill("QA")
    logged_in_page.locator('[data-test="postalCode"]').fill("15143")
    logged_in_page.locator('[data-test="continue"]').click()

    expect(
        logged_in_page.locator('[data-test="inventory-item"]')
    ).to_have_count(2)

    expect(
        logged_in_page.locator('[data-test="subtotal-label"]')
    ).to_have_text("Item total: $39.98")

    expect(
        logged_in_page.locator('[data-test="tax-label"]')
    ).to_have_text("Tax: $3.20")

    expect(
        logged_in_page.locator('[data-test="total-label"]')
    ).to_have_text("Total: $43.18")


def test_user_can_return_home_after_successful_checkout(
    logged_in_page: Page,
):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="firstName"]').fill("Alif")
    logged_in_page.locator('[data-test="lastName"]').fill("QA")
    logged_in_page.locator('[data-test="postalCode"]').fill("15143")
    logged_in_page.locator('[data-test="continue"]').click()
    logged_in_page.locator('[data-test="finish"]').click()

    expect(
        logged_in_page.locator('[data-test="complete-header"]')
    ).to_have_text("Thank you for your order!")

    logged_in_page.locator('[data-test="back-to-products"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(
        logged_in_page.locator('[data-test="inventory-container"]')
    ).to_be_visible()


def test_cancel_checkout_returns_to_cart(logged_in_page: Page):
    logged_in_page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    logged_in_page.locator('[data-test="shopping-cart-link"]').click()
    logged_in_page.locator('[data-test="checkout"]').click()

    logged_in_page.locator('[data-test="cancel"]').click()

    expect(logged_in_page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )
    expect(
        logged_in_page.locator(
            '[data-test="cart-list"] [data-test="inventory-item"]'
        )
    ).to_have_count(1)
    expect(
        logged_in_page.locator('[data-test="shopping-cart-badge"]')
    ).to_have_text("1")
