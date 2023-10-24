from lib.request import *

class Request_repository:
    
    def __init__(self,connection):
        self._connection = connection

    def add_request(self, request_user_id, space_id,requested_date, status):

        new_request = Request(request_user_id, space_id,requested_date, status)
        return f" Added: {new_request.__repr__()}"



