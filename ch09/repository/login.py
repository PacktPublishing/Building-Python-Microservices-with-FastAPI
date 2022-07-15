from typing import Dict, Any
from models.data.orrs import Login, Profile
from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

class LoginRepository: 
    
    def __init__(self, engine): 
        self.engine = engine
        
    async def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
           login = Login(**details)
           login.passphrase = pwd_context.encrypt(login.password)
           await self.engine.save(login)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def add_profile(self, details:Dict[str, Any], username:str) -> bool: 
       try:
          login = await self.engine.find_one(Login, Login.username == username)
                  
          profile = Profile(**details)
          login.profile = profile
          
          await self.engine.save(login)
       except Exception as e:
           print(e) 
           return False 
       return True
    
    
    async def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          login = await self.engine.find_one(Login, Login.login_id == id)
                  
          for key,value in details.items():
            setattr(login,key,value)
          
          await self.engine.save(login)
       except Exception as e:
           print(e) 
           return False 
       return True
   
    async def delete_login(self, id:int) -> bool: 
        try:
            login = await self.engine.find_one(Login, Login.login_id == id) 
            await self.engine.delete(login)
        except: 
            return False 
        return True
    
    async def get_all_login(self):
        logins = await self.engine.find(Login)
        return logins
            
    async def get_login_id(self, id:int): 
        login = await self.engine.find_one(Login, Login.login_id == id) 
        return login
    
    async def get_login_credentials(self, username:str, password:str):
        try:
            login = await self.engine.find_one(Login, Login.username == username) 
            if login == None or not pwd_context.verify(password, login.passphrase): 
                return None 
            else:
                return login
        except:
            return login
    
    async def validate_login(self, username:str):
        try:
            login = await self.engine.find_one(Login, Login.username == username) 
            if login == None: 
                return None 
            else:
                return login
        except:
            return login
        
    async def verify_password(self, username:str, password:str):
        try:
            login = await self.engine.find_one(Login, Login.username == username) 
            if login == None: 
                return False 
            else:
               return pwd_context.verify(password, login.passphrase)
        except:
            return False