from playwright.sync_api import Page, expect

"""
We can render the signup page
"""
def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    heading_tag = page.locator("h1")
    expect(heading_tag).to_have_text("MakersBnB")


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