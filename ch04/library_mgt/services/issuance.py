from typing import Optional
from library_mgt.repository.issuance import BookIssuanceRepository
from library_mgt.models.data.library import BookIssuance
from datetime import datetime
class BookIssuanceService: 
    
    def __init__(self): 
        self.repo:BookIssuanceRepository = BookIssuanceRepository()
        
    def add_book_release(self, book_release:BookIssuance): 
        result = self.repo.insert_approval(book_release)
        return result
    
    def update_book_release(self, approved_id:int, book_id:Optional[int] = None, approver:Optional[str] = None): 
        result = False
        if not book_id == None: 
            result = self.repo.update_approval_details(approved_id, None, approver )
        elif not approver == None: 
            result = self.repo.update_approval_details(approved_id, approver, None )
        return result 
    
    def remove_book_release(self, approved_id:int): 
        result = self.repo.delete_approval(approved_id)
        return result 
    
    def return_issued_book(self, issue_id:int, returned_date:datetime): 
        result = self.repo.return_book(issue_id, returned_date )
        return result
    
    def list_book_release(self): 
        return self.repo.get_all_approvals()