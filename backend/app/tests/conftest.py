import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def chrome_page():
    """Return playwright chromium browser page"""
    playwright_sync = sync_playwright().start()
    chrome_browser = playwright_sync.chromium.launch(
        headless=False, slow_mo=800, timeout=120000
    )
    context = chrome_browser.new_context()

    page = context.new_page()
    yield page

    chrome_browser.close()
    playwright_sync.stop()
