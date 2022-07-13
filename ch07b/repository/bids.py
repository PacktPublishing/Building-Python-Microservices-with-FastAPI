from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Bids

class BidsRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_bid(self, bid: Bids) -> bool: 
        try:
            self.sess.add(bid)
            self.sess.commit()
        except: 
            return False 
        return True
    
    def update_bid(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Bids).filter(Bids.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_bid(self, id:int) -> bool: 
        try:
           auction = self.sess.query(Bids).filter(Bids.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_bids(self):
        return self.sess.query(Bids).all() 
    
    def get_bids_auction_id(self, auction_id:int):
        return self.sess.query(Bids).filter(Bids.auction_id == auction_id).all()
     
    def get_bid(self, id:int): 
        return self.sess.query(Bids).filter(Bids.id == id).one_or_none()