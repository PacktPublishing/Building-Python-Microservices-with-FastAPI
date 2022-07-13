from datetime import datetime
from typing import Optional
from library_mgt.models.data.library import BookIssuance
from library_mgt.models.data.librarydb import book_issuance_tbl

class BookIssuanceRepository: 
    
    def insert_approval(self, approved:BookIssuance): 
        try: 
            book_issuance_tbl[approved.issue_id] = approved
        except: 
            return False
        return True

    def update_approval_details(self, approved_id:int, book_id:Optional[int] = None, approver:Optional[str] = None): 
        approved = book_issuance_tbl[approved_id]
        try: 
            if not book_id == None: 
                approved.book_id = book_id
            elif not approver == None: 
                approved.approved_by = approver
        except: 
            return False
        return True
    
    def delete_approval(self, approved_id:int): 
        try: 
            del book_issuance_tbl[approved_id]
        except: 
            return False
        return True
    
    def return_book(self, issue_id:int, returned_date:datetime): 
        try: 
            issuance = book_issuance_tbl[issue_id]
            issuance.returned_date = returned_date
            book_issuance_tbl[issue_id] = issuance
            
        except: 
            return False
        return True

    def get_all_approvals(self): 
        return book_issuance_tbl