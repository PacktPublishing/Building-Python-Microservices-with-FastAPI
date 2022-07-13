from mongoengine import connect

def create_db():
  global db        
  db = connect(db="obrs", host="localhost", port=27017)
        
def disconnect_db():
    db.close()