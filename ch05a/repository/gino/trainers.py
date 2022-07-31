from models.data.gino_models import Profile_Members, Profile_Trainers, Gym_Class
from typing import Dict, Any

class TrainerRepository: 
    
    async def insert_trainer(self, details:Dict[str, Any]) -> bool: 
        try:
            await Profile_Trainers.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_trainer(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         trainer = await Profile_Trainers.get(id)
         # await Profile_Trainers.update.values(**details).where(Profile_Trainers.id == id).gino.status()
         await trainer.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_trainer(self, id:int) -> bool: 
        try:
            trainer = await Profile_Trainers.get(id)
            await trainer.delete()
            #await Profile_Trainers.delete.where(Profile_Trainers.id == id).gino.status()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_member(self):
        return await Profile_Trainers.query.gino.all()
        
    async def get_member(self, id:int): 
        return await Profile_Trainers.get(id)
    
class GymClassRepository:
        
    async def join_classes_trainer(self):
        query = Gym_Class.join(Profile_Trainers).select()
        result = await query.gino.load(Gym_Class.distinct(Gym_Class.id).load(parent=Profile_Trainers)).all()
        return result 
    
    async def join_member_classes(self):
        query = Gym_Class.join(Profile_Members).select()
        result = await query.gino.load(Profile_Members.distinct(Profile_Members.id).load(add_child=Gym_Class)).all()
        return result 

    async def join_classes_member(self):
        result = await Profile_Members.load(add_child=Gym_Class).query.gino.all()
