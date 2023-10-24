# requests class

class Request:

    def __init__(self, requested_date, space_id, request_user_id, status ):
        
        #initialised variables
        self.id = int
        self.request_user_id = int (request_user_id)
        self.space_id = int (space_id)
        self.requested_date = str (requested_date)
        self.status = bool (status)

    # to set approved 
    def approve_request(self):
        self.status = True

    #for testing equality (to adjust)
    def __eq__(self,other):
        return self== other

    #for string representation
    def __repr__(self):
        return f"Request({self.id}, requested date:{self.requested_date},space id:{self.space_id}, requestor's id:{self.request_user_id},current stats:{self.status})"