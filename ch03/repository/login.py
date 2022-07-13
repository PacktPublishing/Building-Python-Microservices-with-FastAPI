from datetime import date
logs_visitor = dict()

class LoginRepository:
    def __init__(self): 
        pass
    
    def login_audit(self, username: str, password: str):
        logs_visitor[username] = date.today()
