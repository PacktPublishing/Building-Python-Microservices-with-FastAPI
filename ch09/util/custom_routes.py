from fastapi.routing import APIRoute
from typing import Callable
from fastapi import Request, Response
from util.custom_request import CustomRequest, ExtractionRequest, FileRequest, DecryptRequest

class CustomRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            
            request = CustomRequest(request.scope, request.receive)
            response: Response = await original_route_handler(request)
            return response

        return custom_route_handler
    

class ExtractContentRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()
        
        async def custom_route_handler(request: Request) -> Response:
            request = ExtractionRequest(request.scope, request.receive)
            response: Response = await original_route_handler(request)
            return response
        return custom_route_handler
    
class FileStreamRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
           
          
            request = FileRequest(request.scope, request.receive)
            response: Response = await original_route_handler(request)
            return response

        return custom_route_handler
    
class DecryptContentRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
           
          
            request = DecryptRequest(request.scope, request.receive)
            
            response: Response = await original_route_handler(request)
            return response

        return custom_route_handler