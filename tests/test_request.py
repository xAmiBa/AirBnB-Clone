from lib.request import *

def test_approve_request():

    new_request = Request("requested_date", 1, 2 , False)

    new_request.approve_request()
    assert new_request.status == True
