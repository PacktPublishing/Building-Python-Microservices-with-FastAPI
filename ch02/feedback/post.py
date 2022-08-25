from fastapi import APIRouter, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from uuid import UUID, uuid1
from handler_exceptions import PostRatingException, PostFeedbackException

from places.destination import tours, StarRating, Post
from login.user import approved_users
from background import audit_log_transaction
from utility import check_post_owner

        
router = APIRouter()

feedback_tour = dict()

class Assessment(BaseModel):
    id: UUID
    post: Post
    tour_id: UUID
    tourist_id: UUID
    
@router.post("/feedback/add")
def post_tourist_feedback(touristId: UUID, tid: UUID, post: Post, bg_task: BackgroundTasks):
    if approved_users.get(touristId) == None and tours.get(tid) == None:
        raise PostFeedbackException(detail='tourist and tour details invalid', status_code=403)
    assessId = uuid1()
    assessment = Assessment(id=assessId, post=post, tour_id= tid, tourist_id=touristId) 
    feedback_tour[assessId] = assessment
    tours[tid].ratings = (tours[tid].ratings + post.rating)/2
    
    assess_json = jsonable_encoder(assessment)
    bg_task.add_task(audit_log_transaction, str(touristId), message="post_tourist_feedback")
    return JSONResponse(content=assess_json, status_code=200)

@router.post("/feedback/update/rating")
def update_tour_rating(assessId: UUID, new_rating: StarRating):
    print(new_rating)
    if feedback_tour.get(assessId) == None:
        raise PostRatingException(detail='tour assessment invalid', status_code=403)
    tid = feedback_tour[assessId].tour_id
    tours[tid].ratings = (tours[tid].ratings + new_rating)/2
    tour_json = jsonable_encoder(tours[tid])
    return JSONResponse(content=tour_json, status_code=200)

@router.delete("/feedback/delete")
async def delete_tourist_feedback(assessId: UUID, touristId: UUID ):
    if approved_users.get(touristId) == None and feedback_tour.get(assessId):
        raise PostFeedbackException(detail='tourist and tour details invalid', status_code=403)
    post_delete = [access for access in feedback_tour.values() if access.id == assessId]
    for access in post_delete:
        is_owner = await check_post_owner(feedback_tour, access.id, touristId)
        if is_owner:
            del feedback_tour[access.id]
    return JSONResponse(content={"message" : f"deleted posts of {touristId}"}, status_code=200)

@router.get("/feedback/list")
async def show_tourist_post(touristId: UUID):
    print(feedback_tour)
    tourist_posts = [assess for assess in feedback_tour.values() if assess.tourist_id == touristId]
    tourist_posts_json = jsonable_encoder(tourist_posts) 
    return JSONResponse(content=tourist_posts_json, status_code=200)
