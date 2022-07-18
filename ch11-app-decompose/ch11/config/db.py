from motor.motor_asyncio import AsyncIOMotorClient


def create_async_db():
    global client
    client = AsyncIOMotorClient(str("localhost:27017"))

def create_db_collections():
    db = client.osms

    users = db["login"]
    players = db["player"]
    officials = db["official"]
    return {"users": users, "players": players, "officials": officials}

def close_async_db(): 
    client.close()