from playwright.sync_api import Page, expect

"""
We can render the signup page
"""
def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("MakersBnB")

def test_get_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Signup")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Signup to MakersBnB")


