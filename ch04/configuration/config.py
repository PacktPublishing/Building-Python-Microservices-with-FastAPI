from pydantic import BaseSettings
from datetime import date
import os

class FacultySettings(BaseSettings): 
    application:str = 'Faculty Management System' 
    webmaster:str = 'sjctrags@university.com'
    created:date = '2021-11-10'

class LibrarySettings(BaseSettings): 
    application:str = 'Library Management System' 
    webmaster:str = 'sjctrags@university.com'
    created:date = '2021-11-10' 
 

class StudentSettings(BaseSettings): 
    application:str = 'Student Management System' 
    webmaster:str = 'sjctrags@university.com'
    created:date = '2021-11-10'
    
class ServerSettings(BaseSettings): 
    production_server:str
    prod_port:int
    development_server:str 
    dev_port:int
    
    class Config: 
        env_file = os.getcwd() + '/configuration/erp_settings.properties'
        

    
    