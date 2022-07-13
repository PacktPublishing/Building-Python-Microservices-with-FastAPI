from dependency_injector import containers, providers

from repository.users import login_details
from repository.login import LoginRepository
from repository.admin import AdminRepository
from repository.keywords import KeywordRepository
from service.recipe_utilities import get_recipe_names 

class Container(containers.DeclarativeContainer):
    loginservice = providers.Factory(LoginRepository)
    adminservice = providers.Singleton(AdminRepository)
    keywordservice = providers.Factory(KeywordRepository)
    recipe_util = providers.Callable(get_recipe_names) 
    login_repo = providers.Dict(login_details)
    
    
