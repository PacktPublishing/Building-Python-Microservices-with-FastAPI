from pydantic import BaseModel
from datetime import date

class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout:int
    timein:int
    date_log:date