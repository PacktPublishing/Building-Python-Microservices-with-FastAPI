from motor.motor_asyncio import AsyncIOMotorClient


def create_async_db():
    global client
    client = AsyncIOMotorClient(str("localhost:27017"))

def create_db_collections():
    db = client.obrs
    buyers = db["buyer"]
    users = db["login"]
    return {"users": users, "buyers": buyers}

def close_async_db(): 
    client.close()