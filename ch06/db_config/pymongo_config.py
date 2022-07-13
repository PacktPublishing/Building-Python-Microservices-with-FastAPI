from pymongo import MongoClient

def create_db_collections():
    client = MongoClient('mongodb://localhost:27017/')
    try:
        db = client.obrs
        buyers = db.buyer
        users = db.login
        yield {"users": users, "buyers": buyers}
    finally:
        client.close()

    
    

