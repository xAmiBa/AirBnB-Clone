from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("MakersBnB")