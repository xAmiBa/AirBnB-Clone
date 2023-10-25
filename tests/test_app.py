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


# def test_for_signup_errors(page, test_web_address):
#     page.goto(f"http://{test_web_address}/signup")
#     page.fill("input[name=name]", "Test name")
#     page.fill("input[name=username]", "Test username")
#     page.fill("input[name=email]", "test@email.com")
#     page.fill("input[name=password]", "Test password")
#     page.click("text=signup")
#     h2_tag = page.locator("h2")
#     expect(h2_tag).to_have_text("Thank you, you are signed up! Now login.")
    
