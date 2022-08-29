from mongoframes.factory.makers import  Q
from models.data.mongoframe import Category, Reference
from typing import List, Dict, Any 


class ReferenceRepository:
    
    def insert_reference(self, details:Dict[str, Any]) -> bool: 
        try:
           reference = Reference(**details)
           reference.insert()
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    def add_category(self, id:int, details:Dict[str, Any]) -> bool:
        try:
            item = Category(**details)
            reference = Reference.one(Q.id==id)
            if reference.categories == None:
                reference.categories = list()
            reference.categories.append(item)
            reference.update()
        except:
           return False 
        return True
    
    def get_category(self, id:int, cat_id:int) -> Category:
        try:
            reference = Reference.one(Q.id==id)
            category = [c for c in reference.categories if c["id"] == cat_id]
            return category[0]
        except: 
           return None 
        
    def get_all_categories(self, id:int) -> List[Category]: 
        try:
            reference = Reference.one(Q.id==id)   
            return reference.categories
        except: 
           return None 
       
    def update_reference(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
            reference = Reference.one(Q.id == id)
            for key,value in details.items():
                setattr(reference,key,value)
            reference.update()
       except: 
           return False 
       return True
   
    def delete_reference(self, id:int) -> bool: 
        try:
           reference = Reference.one(Q.id == id)
           reference.delete()
        except: 
            return False 
        return True
    
    def get_all_reference(self):
        references = [ref.to_json_type() for ref in Reference.many()]
        return references
    
    def get_reference(self, id:int): 
        reference = Reference.one(Q.id == id).to_json_type()
        return reference