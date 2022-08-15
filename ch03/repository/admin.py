
from repository.users import login_details, user_profiles
from repository.login import logs_visitor

class AdminRepository:
    
    def __init__(self): 
        pass
    
    def query_login_details(self): 
        return list(login_details.values()) 
    
    def query_user_profiles(self): 
        return list(user_profiles.values())
    
    def query_logs_visitor(self): 
        return list(logs_visitor.values())