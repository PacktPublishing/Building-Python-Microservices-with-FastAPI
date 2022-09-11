
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.data.pccs_beanie import Login, Profile

async def db_connect():
    global client
    client = AsyncIOMotorClient(f"mongodb://localhost:27017/pccs")
    await init_beanie(client.pccs, document_models=[Login, Profile])
   
        
async def db_close():
    client.close()