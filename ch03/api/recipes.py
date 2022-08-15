from fastapi import APIRouter, Depends
from service.factory import get_recipe_service
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from model.recipes import Recipe
from model.classifications import Category, Origin
from typing import List
from uuid import UUID

class IngredientReq(BaseModel):
    id: UUID 
    name:str
    qty : int
    measure : str
      
        
class RecipeReq(BaseModel):
    id: UUID 
    name: str
    ingredients: List[IngredientReq]
    cat: Category
    orig : Origin
     
        
router = APIRouter()

@router.post("/recipes/insert")
def insert_recipe(recipe: RecipeReq, handler=Depends(get_recipe_service)): 
    json_dict = jsonable_encoder(recipe)
    rec = Recipe(**json_dict)
    handler.add_recipe(rec)
    return JSONResponse(content=json_dict, status_code=200)

@router.get("/recipes/list/all")
def get_all_recipes(handler=Depends(get_recipe_service)):
    return handler.get_recipes()
