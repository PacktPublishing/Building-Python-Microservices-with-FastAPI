
from typing import Dict, Any

from sqlalchemy import update, delete, insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.data.sqlalchemy_async_models import Attendance_Member
from datetime import datetime

class AttendanceRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_attendance(self, attendance: Attendance_Member) -> bool: 
        try:
            sql = insert(Attendance_Member).values(id=attendance.id, member_id=attendance.member_id, timein=datetime.strptime(attendance.timein, "%H:%M"), timeout=datetime.strptime(attendance.timeout, "%H:%M"), date_log=attendance.date_log)
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
            
            #self.sess.add(attendance)
            #await self.sess.flush()
        except: 
            return False 
        return True
    
    async def update_attendance(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
           details["timeout"] = datetime.strptime(details["timeout"] , "%H:%M")
           details["timein"] = datetime.strptime(details["timein"] , "%H:%M")
           sql = update(Attendance_Member).where(Attendance_Member.id == id).values(**details)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
           
       except: 
           return False 
       return True
   
    async def delete_attendance(self, id:int) -> bool: 
        try:
           sql = delete(Attendance_Member).where(Attendance_Member.id == id)
           sql.execution_options(synchronize_session="fetch")
           await self.sess.execute(sql)
        except: 
            return False 
        return True
    
    async def get_all_attendance(self):
        q = await self.sess.execute(select(Attendance_Member))
        return q.scalars().all()
    
    async def get_attendance(self, id:int): 
        q = await self.sess.execute(select(Attendance_Member).where(Attendance_Member.member_id == id))
        return q.scalars().all()

    async def check_attendance(self, id:int): 
        q = await self.sess.execute(select(Attendance_Member).where(Attendance_Member.id == id))
        return q.scalar()
    