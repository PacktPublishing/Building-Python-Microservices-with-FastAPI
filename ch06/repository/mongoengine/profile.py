from typing import Dict, Any
from models.data.mongoengine import Login, UserProfile, BookForSale

class UserProfileRepository(): 
    
    def insert_profile(self, login_id:int, details:Dict[str, Any]) -> bool: 
        try:
            profile = UserProfile(**details)
            login = Login.objects(id=login_id).get()
            login.update(profile=profile)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def add_book_sale(self, login_id:int, details:Dict[str, Any]): 
        try:
            sale = BookForSale(**details)
            login = Login.objects(id=login_id).get()
            login.profile.booksale.append(sale)
                       
            login.update(profile=login.profile)
        except Exception as e:
            print(e)
            return False 
        return True 
    
    def delete_book_sale(self, login_id:int, book_id:int):
        try:
            login = Login.objects(id=login_id).get()
            booksale = [b for b in login.profile.booksale if b.id == book_id]
            login.profile.booksale.remove(booksale[0])
            login.update(profile=login.profile)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def update_profile(self, login_id:int, details:Dict[str, Any]) -> bool: 
       try:
          profile = UserProfile(**details)
          login = Login.objects(id=login_id).get()
          login.update(profile=profile)
       except: 
           return False 
       return True
   
    def delete_profile(self, login_id:int) -> bool: 
        try:
            login = Login.objects(id=login_id).get()
            login.update(unset__profile=1)
        except: 
            return False 
        return True
    
    def block_profile(self, login_id:int)->bool: 
        try:
            login = Login.objects(id=login_id).get()
            profile = login.profile
            profile.status = False
            login.update(profile=profile)
        except: 
            return False 
        return True
    
    def get_all_profile(self):
        profiles = Login.objects.filter(profile__login_id__exists=True)
        profiles_dict = list(map(lambda h: h.profile.to_json(), Login.objects().filter(profile__login_id__exists=True)))
        return profiles_dict
    
    def get_profile(self, login_id:int): 
        login = Login.objects(id=login_id).get()
        profile = login.profile.to_json()
        return profile