import pytest
from playwright.sync_api import sync_playwright

def test_duckduckgo_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://duckduckgo.com")

        page.fill("input[name='q']", "Playwright Python")
        page.keyboard.press("Enter")

        page.wait_for_selector("a.result__a")  # Updated locator for search results

        assert "Playwright" in page.content()

        browser.close()
