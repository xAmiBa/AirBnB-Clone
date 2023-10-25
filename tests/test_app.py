from playwright.sync_api import Page, expect

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
    
    
def test_for_incorrect_login(page, test_web_address):
    # go to page
    page.goto(f"http://{test_web_address}/login")
    # input details
    page.fill("input[name=email]", "tony@test.com")
    page.fill("input[name=password]", "tony")
    page.click("text=Login")
    errors_tag = page.locator(".t-errors")
    page.screenshot(path="screenshot.png", full_page=True)
    expect(errors_tag).to_have_text(
        ["There were errors with your submission:\n\n\n Incorrect details. \n\n"]
        )
    

"""
# list a new space
# # [POST] /spaces/new -- template = new_place.html
# # Posts a new space listing
# # @app.route('/spaces/new', methods=['POST'])
# """
# def test_list_new_space(db_connection, page, test_web_address):
#     db_connection.seed("seeds/db_makers_bnb.sql")
#     page.goto(f"http://{test_web_address}/spaces/new")

#     page.fill("input[name='name']", "The place")
#     page.fill("input[name='description']", 'The most amazing place to sleep')
#     page.fill("input[name='price']", "50.0")
#     page.fill("input[name='available_from']", '01/01/2024')
#     page.fill("input[name='available_to']", '01/02/2024')

#     page.click("text = List my Space")

#     assert 

    # name_element = page.locator("name")
    # expect(name_element).to_have_text("The place")

    # name_element = page.locator("description")
    # expect(name_element).to_have_text('The most amazing place to sleep')

    # name_element = page.locator(".t-price")
    # expect(name_element).to_have_text(50.0)

    # name_element = page.locator(".t-available_from")
    # expect(name_element).to_have_text("01/01/2024")

    # name_element = page.locator(".t-available_to")
    # expect(name_element).to_have_text("01/02/2024")    
