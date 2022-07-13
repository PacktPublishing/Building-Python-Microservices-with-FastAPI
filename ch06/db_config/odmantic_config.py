from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

def create_db_connection():
   global client_od
   client_od = AsyncIOMotorClient(f"mongodb://localhost:27017/")

def create_db_engine():
   engine = AIOEngine(motor_client=client_od, database="obrs")
   return engine

def close_db_connection():
    client_od.close()
