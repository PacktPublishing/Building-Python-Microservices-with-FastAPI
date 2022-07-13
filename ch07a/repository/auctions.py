from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Auctions

class AuctionsRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_auction(self, auc: Auctions) -> bool: 
        try:
            self.sess.add(auc)
            self.sess.commit()
        except: 
            return False 
        return True
    
    def update_auction(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Auctions).filter(Auctions.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_auction(self, id:int) -> bool: 
        try:
           auction = self.sess.query(Auctions).filter(Auctions.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_auctions(self):
        return self.sess.query(Auctions).all() 
    
    def get_auctions_profile_id(self, profile_id:int):
        return self.sess.query(Auctions).filter(Auctions.profile_id == profile_id).all()
     
    def get_auction(self, id:int): 
        return self.sess.query(Auctions).filter(Auctions.id == id).one_or_none()