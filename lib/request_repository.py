from lib.request import *

class Request_repository:
    
    def __init__(self,connection):
        self._connection = connection

    def add_request(self, request_user_id, space_id,requested_date, status):

        new_request = Request(request_user_id, space_id,requested_date, status)
        self._connection.execute('INSERT INTO requests (request_user_id, space_id, requested_date, status) VALUES (%s, %s, %s, %s)', [
                                new_request.request_user_id, new_request.space_id, new_request.requested_date, new_request.status])
        return None

    def get_all_requests(self, db_connection):
        rows = self._connection.execute('SELECT * from requests')
        requests = []
        for row in rows:
            item = Request(row["id"], row["request_user_id"], row["space_id"], row["requested_date"], row["status"])
            requests.append(item)
        return requests

