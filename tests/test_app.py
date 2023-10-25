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


def test_for_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.fill("input[name=name]", "Test name")
    page.fill("input[name=username]", "Test username")
    page.fill("input[name=email]", "email@email")
    page.fill("input[name=password]", "Test password")
    page.click("text=Signup to MarkersBnB")
    h2_tag = page.locator("h2")
    page.screenshot(path="screenshot.png", full_page=True)
    expect(h2_tag).to_have_text("Thank you, you are signed up! Now login.")
    

def test_for_error_exiting_user_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.fill("input[name=name]", "Test name")
    page.fill("input[name=username]", "Jake_1")
    page.fill("input[name=email]", "email@email")
    page.fill("input[name=password]", "Test password")
    page.click("text=Signup to MarkersBnB")
    errors_tag = page.locator(".t-errors")
    page.screenshot(path="screenshot.png", full_page=True)
    expect(errors_tag).to_have_text(
        ["There were errors with your submission:\n\n\nThis email or username is alredy registered.\n\n"]
        )
    
    
