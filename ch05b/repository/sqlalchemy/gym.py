
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.data.sqlalchemy_async_models import Gym_Class
from datetime import datetime

class GymRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_gymclass(self, gym: Gym_Class) -> bool: 
        try:
            sql = insert(Gym_Class).values(id=gym.id, name=gym.name, member_id=gym.member_id, trainer_id=gym.trainer_id, approved=gym.approved)
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
            
            #self.sess.add(attendance)
            #await self.sess.flush()
        except:
            return False 
        return True
    
    async def update_gymclass(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           sql = update(Gym_Class).where(Gym_Class.id == id).values(**details)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
           
       except Exception as e: 
           print(e)
           return False 
       return True
   
    async def delete_gymclass(self, id:int) -> bool: 
        try:
           sql = delete(Gym_Class).where(Gym_Class.id == id)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
        except: 
            return False 
        return True
    
    async def get_all_gymclass(self):
        q = await self.sess.execute(select(Gym_Class))
        return q.scalars().all()
    
    async def get_gymclass(self, id:int): 
        q = await self.sess.execute(select(Gym_Class).where(Gym_Class.id == id))
        return q.scalars().all()