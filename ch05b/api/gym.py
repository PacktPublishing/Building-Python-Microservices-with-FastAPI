from fastapi import APIRouter
from db_config.sqlalchemy_async_connect import AsynSessionFactory
from repository.sqlalchemy.gym import GymRepository
from models.requests.gym import GymClassReq
from models.data.sqlalchemy_async_models import Gym_Class
router = APIRouter()

@router.post("/gym/class/add")
async def add_gym_class(req:GymClassReq ):
    async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = GymRepository(sess)
            gym_class = Gym_Class(id=req.id, name=req.name, member_id=req.member_id, trainer_id=req.trainer_id, approved=req.approved)
            return await repo.insert_gymclass(gym_class)
        
@router.patch("/gym/class/update")
async def update_gym_class(id:int, req:GymClassReq ):
    async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = GymRepository(sess)
            gym_class_dict = req.dict(exclude_unset=True)
            return await repo.update_gymclass(id, gym_class_dict)

@router.delete("/gym/class/delete/{id}")
async def delete_gym_class(id:int): 
     async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = GymRepository(sess)
            return await repo.delete_gymclass(id)

@router.get("/gym/class/list")
async def list_gym_class():
     async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = GymRepository(sess)
            return await repo.get_all_gymclass()

@router.get("/gym/class/{id}")
async def get_gym_class(id:int):
    async with AsynSessionFactory() as sess:
        async with sess.begin():
            repo = GymRepository(sess)
            return await repo.get_gymclass(id)