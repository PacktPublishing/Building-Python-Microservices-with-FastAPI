from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import db
from models.requests.trainers import ProfileTrainersReq
from repository.gino.trainers import TrainerRepository, GymClassRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.queries import ProfileTrainerListQuery
from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler

async def sess_db():
    await db.set_bind("postgresql+asyncpg://postgres:admin2255@localhost:5433/fcms")
    
router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/trainer/add" )
async def add_trainer(req: ProfileTrainersReq): 
    handler = AddTrainerCommandHandler()
    mem_profile = dict()
    mem_profile["id"] = req.id
    mem_profile["firstname"] = req.firstname
    mem_profile["lastname"] = req.lastname
    mem_profile["age"] = req.age
    mem_profile["position"] = req.position
    mem_profile["tenure"] = req.tenure
    mem_profile["shift"] = req.shift
    command = ProfileTrainerCommand()
    command.details = mem_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create trainer profile problem encountered'}, status_code=500) 

@router.patch("/trainer/update" )
async def update_trainer(id:int, req: ProfileTrainersReq): 
    mem_profile_dict = req.dict(exclude_unset=True)
    repo = TrainerRepository()
    result = await repo.update_trainer(id, mem_profile_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)

@router.delete("/trainer/delete/{id}")
async def delete_delete(id:int):
    repo = TrainerRepository()
    result = await repo.delete_trainer(id )
    if result: 
        return JSONResponse(content={'message':'profile delete successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete profile error'}, status_code=500)
    
@router.get("/trainer/list")
async def list_trainers(): 
    handler = ListTrainerQueryHandler()
    query:ProfileTrainerListQuery = await handler.handle() 
    return query.records

@router.get("/classes/trainers/list")
async def list_classes_trainers(): 
    repo = GymClassRepository()
    return await repo.join_classes_trainer()

@router.get("/classes/members/list")
async def list_classes_members(): 
    repo = GymClassRepository()
    return await repo.join_member_classes()

@router.get("/members/classes/list")
async def list_members_classes(): 
    repo = GymClassRepository()
    return await repo.join_classes_member()
