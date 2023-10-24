from lib.request import *

class Request_repository:
    
    # setup connection
    def __init__(self,connection):
        self._connection = connection

    # adding a request, taking a request object
    def add_request(self, request):

        self._connection.execute('INSERT INTO requests (request_user_id, space_id, requested_date, status) VALUES (%s, %s, %s, %s)', [
                                request.request_user_id, request.space_id, request.requested_date, request.status])
        return None

    # getting list of all requests
    def get_all_requests(self):
        rows = self._connection.execute('SELECT id, request_user_id, space_id, requested_date, status from requests')
        requests = []
        for row in rows:
                    # setting requests with the 5 variables
            item = Request( row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
            requests.append(item)
        return requests

