# SauceDemo Web Automation Testing

A web UI automation testing project built with **Python, Playwright, and pytest** to validate core e-commerce user flows on [SauceDemo](https://www.saucedemo.com/).

## Project Overview

This project covers functional, negative, regression, and end-to-end testing for essential e-commerce workflows.

### Test Coverage

| Module | Coverage |
|---|---|
| Login | Valid credentials, invalid password, empty username, empty password |
| Products | Product listing, sorting, product details, add to cart |
| Shopping Cart | Add/remove products, multiple items, empty cart, cart persistence |
| Checkout | Successful checkout, required-field validation, order summary, cancel checkout |
| Navigation | Logout, sidebar navigation, About page, session validation |

## Tech Stack

- Python 3.14
- Playwright
- pytest
- pytest-playwright
- pytest-html

## Project Structure

```text
saucedemo-playwright/
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_navigation.py
├── reports/
├── screenshots/
├── test-results/
├── requirements.txt
└── README.md
```

## Prerequisites

- Python installed
- Git (optional, for version control)
- Internet access to reach SauceDemo

## Installation

Clone the repository and enter the project directory:

```bash
git clone <your-github-repository-url>
cd saucedemo-playwright
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Running Tests

Run the complete test suite:

```powershell
python -m pytest -v
```

Generate an HTML report:

```powershell
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
python -m pytest -v --output=test-results "--html=reports/test-report-$timestamp.html" --self-contained-html
```

Open the generated HTML report in a browser to review the test results.

## Failure Screenshots

The project includes a pytest hook that attempts to capture a screenshot when a test fails. Screenshots are saved in the `screenshots/` directory.

## Test Results

The latest recorded regression run passed **30 tests**, with one warning. Results may vary when tests are run again.

## Scope and Limitations

- UI automation is implemented with Playwright and pytest.
- Tests require access to the SauceDemo website.
- This project currently focuses on web UI testing.
- Test results depend on the application's availability and behavior.

## Author

QA Tester | Functional Testing | Regression Testing | Web Automation | Python & Playwright