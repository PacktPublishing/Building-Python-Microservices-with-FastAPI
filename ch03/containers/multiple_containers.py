
from dependency_injector import containers, providers

from repository.login import LoginRepository
from repository.admin import AdminRepository
from repository.keywords import KeywordRepository

class KeywordsContainer(containers.DeclarativeContainer): 
    keywordservice = providers.Factory(KeywordRepository)

class AdminContainer(containers.DeclarativeContainer): 
    adminservice = providers.Singleton(AdminRepository)

class LoginContainer(containers.DeclarativeContainer): 
    loginservice = providers.Factory(LoginRepository)
    
class RecipeAppContainer(containers.DeclarativeContainer): 
    keywordcontainer = providers.Container(KeywordsContainer)
    admincontainer = providers.Container(AdminContainer)
    logincontainer = providers.Container(LoginContainer)