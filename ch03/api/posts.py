from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from dependencies.posts import check_feedback_length
from model.classifications import RecipeRating
from model.posts import Post
from service.factory import get_post_service
from uuid import UUID
from datetime import date

router = APIRouter()

async def create_post(id:UUID, feedback: str, rating: RecipeRating, userId: UUID, date_posted: date): 
    post = {"id": id, "feedback": feedback, "rating": rating, "userId" : userId, "date_posted": date_posted}
    return post

@router.post("/posts/insert", dependencies=[Depends(check_feedback_length)])
async def insert_post_feedback(post=Depends(create_post), handler=Depends(get_post_service)): 
    print('hello')
    post_dict = jsonable_encoder(post)
    
    post_obj = Post(**post_dict)
    
    handler.add_post(post_obj)
    return post
    
