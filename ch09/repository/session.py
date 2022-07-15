from typing import Dict, Any
from models.data.orrs import DbSession

class DbSessionRepository: 
    
    def __init__(self, engine): 
        self.engine = engine
        
    async def insert_session(self, details:Dict[str, Any]) -> bool: 
        try:
           exist_sess = await self.engine.find_one(DbSession, DbSession.session_name == details['session_name']) 
           if exist_sess == None:
                session = DbSession(**details)
                print(session)
                await self.engine.save(session)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
   
    async def delete_session(self, name:str) -> bool: 
        try:
            keyword = await self.engine.find_one(DbSession, DbSession.session_name == name) 
            await self.engine.delete(keyword)
        except: 
            return False 
        return True
    
    async def get_all_session(self):
        sessions = await self.engine.find(DbSession)
        return sessions
            
    async def get_session(self, key:str): 
        session = await self.engine.find_one(DbSession, DbSession.session_key == key) 
        return session