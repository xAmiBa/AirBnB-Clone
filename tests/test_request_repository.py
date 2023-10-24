from lib.request_repository import *

def test_request_add():

    new_repo = Request_repository
    new_repo.add_request ( 2, 1, "13/2/23", False)

    assert new_request.request_user_id == 2
    assert new_request.space_id == 1
    assert new_request.requested_date == "13/2/23"
    assert new_request.password == False
