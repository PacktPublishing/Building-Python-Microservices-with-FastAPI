from pydantic import BaseModel
from datetime import date
from typing import Dict

class SurveyDataResult(BaseModel):
   results: Dict[str, int]
    