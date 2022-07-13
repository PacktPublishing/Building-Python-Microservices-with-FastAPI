from library_mgt.models.data.library import BookRequest
from library_mgt.models.data.librarydb import book_request_tbl

class BookRequestRepository: 
    
    def insert_request(self, request:BookRequest): 
        try: 
            book_request_tbl[request.req_id] = request
        except: 
            return False
        return True

    def update_requested_book(self, req_id:int, book_id:int): 
        try: 
            request = book_request_tbl[req_id]
            request.book_id = book_id
        except: 
            return False
        return True
    
    def delete_request(self, req_id:int): 
        try: 
            del book_request_tbl[req_id]
        except: 
            return False
        return True
    
    def get_all_requests(self): 
        return book_request_tbl