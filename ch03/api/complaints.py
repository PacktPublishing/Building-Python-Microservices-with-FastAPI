from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from lagom import Container
from lagom.integrations.fast_api import FastApiIntegration

from repository.recipes import recipes
from repository.complaints import BadRecipeRepository
from uuid import UUID


container = Container()
container[BadRecipeRepository] = BadRecipeRepository()
#container[BadRecipeRepository] = Singleton(BadRecipeRepository) #another way

router = APIRouter()
deps = FastApiIntegration(container, request_singletons=[BadRecipeRepository])

@router.post("/complaint/recipe")
def report_recipe(rid: UUID, complaintservice=deps.depends(BadRecipeRepository)): 
    complaintservice.add_bad_recipe(rid)
    return JSONResponse(content={"message": "reported bad recipe"}, status_code=201)

@router.get("/complaint/list/all")
def list_defective_recipes(complaintservice=deps.depends(BadRecipeRepository)): 
    defects_list = jsonable_encoder(complaintservice.query_bad_recipes())
    return defects_list
