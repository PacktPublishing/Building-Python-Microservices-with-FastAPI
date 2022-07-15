from typing import Dict, Any
from models.data.orrs import Keyword

class KeyRepository: 
    
    def __init__(self, engine): 
        self.engine = engine
        
    async def insert_keyword(self, details:Dict[str, Any]) -> bool: 
        try:
           keyword = Keyword(**details)
           print(keyword)
           await self.engine.save(keyword)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_keyword(self, word:str, details:Dict[str, Any]) -> bool: 
       try:
          keyword = await self.engine.find_one(Keyword, Keyword.word == word)
                  
          for key,value in details.items():
            setattr(keyword,key,value)
          
          await self.engine.save(keyword)
       except Exception as e:
           print(e) 
           return False 
       return True
   
    async def delete_keyword(self, word:str) -> bool: 
        try:
            keyword = await self.engine.find_one(Keyword, Keyword.word == word) 
            await self.engine.delete(keyword)
        except: 
            return False 
        return True
    
    async def get_all_keyword(self):
        keywords = await self.engine.find(Keyword)
        return keywords
            
    async def get_keyword(self, word:str): 
        login = await self.engine.find_one(Keyword, Keyword.word == word) 
        return login