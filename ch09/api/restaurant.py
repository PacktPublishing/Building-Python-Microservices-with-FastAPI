from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, PlainTextResponse, RedirectResponse
from fastapi.templating import Jinja2Templates 
from fastapi.encoders import jsonable_encoder
from models.request.restaurant import RestaurantReq
from models.request.feedback import FeedbackReq
from models.request.food_rate import FoodRateReq 
from models.request.ambiance_rate import AmbianceRateReq 

from config.db import  create_db_engine
from repository.restaurant import RestaurantRepository
from util.json_date import json_datetime_serializer
from util.auth_session import get_current_user
from util.custom_routes import CustomRoute
from cryptography.fernet import Fernet
import os


from json import dumps, loads

from fastapi import File, UploadFile
from fastapi.responses import StreamingResponse
from models.documentation.response import Error500Model

from io import BytesIO
from PIL import Image, ImageFilter
templates = Jinja2Templates(directory="templates")

key = Fernet.generate_key()

router = APIRouter()
router.route_class = CustomRoute
        
@router.post("/restaurant/add",
     summary="This API adds new restaurant details.",
     description="This operations adds new record to the database. ",
     response_description="The message body.",
     responses={
        200: {
            "content": {
                "application/json": {
                    "example": {
                        "restaurant_id": 100,
                        "name": "La Playa",
                        "branch": "Manila",
                        "address": "Orosa St.",
                        "province": "NCR",
                        "date_signed": "2022-05-23",
                        "city": "Manila",
                        "country": "Philippines",
                        "zipcode": 1603
                    }
                }
            },
        },
        404: {
            "description": "An error was encountered during saving.",
            "content": {
                "application/json": {
                    "example": {"message": "insert login unsuccessful"}
                }
            },
        },
    },
    tags=["operation"],)

async def add_restaurant(req:RestaurantReq, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    restaurant_dict = req.dict(exclude_unset=True) 
    restaurant_json = dumps(restaurant_dict, default=json_datetime_serializer)
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.insert_restaurant(loads(restaurant_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert login unsuccessful"}, status_code=500)

@router.post("/restaurant/feedback/add")
async def add_feedback(req:FeedbackReq, id:int, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    feedback_dict = req.dict(exclude_unset=True) 
    feedback_json = dumps(feedback_dict, default=json_datetime_serializer) 
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.add_feedback(id, loads(feedback_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "add feedback unsuccessful"}, status_code=500)

@router.post("/restaurant/ambiance/rate/add")
async def add_ambiance_rate(req: AmbianceRateReq, id:int, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    ambiance_dict = req.dict(exclude_unset=True) 
    ambiance_json = dumps(ambiance_dict, default=json_datetime_serializer) 
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.add_ambience_rating(id, loads(ambiance_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "add ambiance rating unsuccessful"}, status_code=500) 

@router.post("/restaurant/food/rate/add")
async def add_food_rate(req:FoodRateReq, id:int, engine=Depends(create_db_engine), user: str = Depends(get_current_user)): 
    food_dict = req.dict(exclude_unset=True) 
    food_json = dumps(food_dict, default=json_datetime_serializer) 
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.add_food_rating(id, loads(food_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "add food rating unsuccessful"}, status_code=500) 

@router.post("/restaurant/upload/logo")
async def logo_upload_png(logo: UploadFile = File(...)):
    original_image = Image.open(logo.file)
    original_image = original_image.filter(ImageFilter.SHARPEN)

    filtered_image = BytesIO()
    
    if logo.content_type == "image/png":
        original_image.save(filtered_image, "PNG")
        filtered_image.seek(0)
        return StreamingResponse(filtered_image, media_type="image/png")
    elif logo.content_type == "image/jpeg":
        original_image.save(filtered_image, "JPEG")
        filtered_image.seek(0)
        return StreamingResponse(filtered_image, media_type="image/jpeg")

@router.get("/restaurant/list/all")
async def list_restaurants(request: Request, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.get_all_restaurant()
    resto_names = [resto.name for resto in result]
    request.session['resto_names'] = resto_names
    return result

@router.get("/restaurant/list/names")
async def list_restaurant_names(request: Request, user: str = Depends(get_current_user)):
    resto_names = request.session['resto_names']
    return resto_names

@router.get("/restaurant/form/upload/logo")
async def logo_upload_png_form(req: Request, user: str = Depends(get_current_user) ):
    return templates.TemplateResponse("upload_file.html", {"request": req})

@router.get("/restaurant/upload/video",responses={
        200: {
            "content": {"video/mp4": {}},
            "description": "Return an MP4 encoded video.",
        },
        500:{
            "model": Error500Model, 
            "description": "The item was not found"
        }
    },)
def video_presentation():
    file_path = os.getcwd() + '\\files\\sample.mp4'
    def load_file():  
        with open(file_path, mode="rb") as video_file:  
            yield from video_file  
    return StreamingResponse(load_file(), media_type="video/mp4")


@router.get("/restaurant/michelin")
def redirect_restaurants_rates():
  return RedirectResponse(url="https://guide.michelin.com/en/restaurants")

@router.get("/restaurant/index")
def intro_list_restaurants():
  return PlainTextResponse(content="The Restaurants")

@router.get("/restaurant/enc/details")
async def send_enc_login(engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    repo:RestaurantRepository = RestaurantRepository(engine)
    result = await repo.get_all_restaurant();
   
    result_json = dumps(jsonable_encoder(result))
    fernet = Fernet(key)
    enc_data = fernet.encrypt(bytes(result_json, encoding='utf8'))
    
    return {"enc_data" : enc_data, "key": key}