from typing import List, Any, Optional
from models.data.gino_models import Profile_Trainers

class ProfileTrainerListQuery: 
    
    def __init__(self): 
        self._records:List[Profile_Trainers] = list()
        
    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, records):
        self._records = records
        

class ProfileTrainerRecordQuery: 
    
    def __init__(self): 
        self._record:Profile_Trainers = None
        
    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, record):
        self._record = record