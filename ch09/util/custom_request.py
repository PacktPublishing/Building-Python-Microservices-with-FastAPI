from fastapi import Request
from cryptography.fernet import Fernet
import ast
import json
import base64

class CustomRequest(Request):
    async def body(self) -> bytes:
        if hasattr(self, '_body'):
            print('restaurant')
        body = await super().body()
        print('body')
        print(body)
        return body
    
class CustomFormRequest(Request):
    async def form(self) -> bytes:
        if hasattr(self, '_body'):
            print('restaurant')
        body = await super().form()
        print('body')
        print(body)
        return body
    
class CustomJsonRequest(Request):
    
    async def form(self) -> bytes:
       
        body = await super().form()
        print('body')
        print(body)
        return body
    
class ExtractionRequest(Request):
    async def body(self):
        body = await super().body()
        data = ast.literal_eval(body.decode('utf-8'))
        if isinstance(data, list):
            sum = 0
            for rate in data:
                sum += rate 
            average = sum / len(data)
            self.state.sum = sum 
            self.state.avg = average
       
        return body 
    
    async def form(self):
        body = await super().form()
        user_details = dict()
        user_details['fname'] = body['firstname']
        user_details['lname'] = body['lastname']
        user_details['age'] = body['age']
        user_details['bday'] = body['birthday']
        self.session["user_details"] = user_details
        
        return body
    
    async def json(self):
        body = await super().json()
        if isinstance(body, dict):
                
            sum = 0
            for rate in body.values():
                sum += rate  
                    
            average = sum / len(body.values())
            self.state.sum = sum 
            self.state.avg = average
        return body

class FileRequest(Request):
       async def form(self) -> bytes:
              
        body = await super().body()
      
        rv = base64.b64encode(body).decode('utf-8')
        try:
            print(rv)
        except Exception as e:
            print(e)
        
        return body
    
class DecryptRequest(Request):
    async def body(self):
        body = await super().body()
        login_dict = ast.literal_eval(body.decode('utf-8'))
        fernet = Fernet(bytes(login_dict['key'], encoding='utf-8'))
        data = fernet.decrypt(bytes(login_dict['enc_login'], encoding='utf-8'))
        self.state.dec_data = json.loads(data.decode('utf-8'))
        return body