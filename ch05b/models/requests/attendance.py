from pydantic import BaseModel
from datetime import date

class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout:str
    timein:str
    date_log:date