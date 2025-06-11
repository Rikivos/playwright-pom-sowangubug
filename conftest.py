import pytest
from playwright.sync_api import sync_playwright
import config

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        if config.BROWSER == "chrome":
            browser = p.chromium.launch(channel="chrome", headless=False)
        elif config.BROWSER == "chromium":
            browser = p.chromium.launch(headless=False)
        elif config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=False)
        elif config.BROWSER == "webkit":
            browser = p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unknown browser: {config.BROWSER}")

        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config.TIMEOUT * 1000)
    yield page
    context.close()
