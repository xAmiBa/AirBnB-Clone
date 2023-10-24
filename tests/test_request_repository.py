from lib.request_repository import *

def test_request_add():

    new_repo = Request_repository
    new_repo.add_request ( 2, 1, "13/2/23", False)

    assert new_request.request_user_id == 2
    assert new_request.space_id == 1
    assert new_request.requested_date == "13/2/23"
    assert new_request.password == False


def test_get_all_users(db_connection):
    
    db_connection.seed("seeds/db_makers_bnb.sql")
    new_repository = Request_repository(db_connection)
    
    all_requests = new_repository.all()
    assert all_requests == [Request(1,1,2, '12/12/23',False), \
                            Request(2,2,3,'03/08/23',False)]