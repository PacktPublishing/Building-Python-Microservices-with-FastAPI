from survey.tables import Answers
from typing import Dict, List, Any

class AnswerRepository:
    async def insert_answer(self, details:Dict[str, Any]) -> bool: 
        try:
            
            answer = Answers(**details)
            await answer.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_answer(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         answer = await Answers.objects().get(Answers.id == id)
         for key, value in details.items():
            setattr(answer, key, value)
         await answer.save()
       except: 
           return False 
       return True
   
    async def delete_answer(self, id:int) -> bool: 
        try:
            answer = await Answers.objects().get(Answers.id == id)
            await answer.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_answer(self):
        return await Answers.select().order_by(Answers.id)
        
    async def get_answer(self, id:int): 
        return await Answers.objects().get(Answers.id == id)
    
    async def get_answers_per_q(self, loc_id:int, qid:int):
        return await Answers.select(Answers.answer_choice
                                    ).where((Answers.respondent_id.location_id == loc_id) & (Answers.question_id == qid))