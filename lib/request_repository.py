from lib.request import *

class Request_repository:
    
    def __init__(self,connection):
        self._connection = connection

    def add_request(self, requested_date, space_id, request_user_id, status):

        new_request = Request(requested_date, space_id, request_user_id, status)
        return f" Added: {new_request.__repr__()}"



