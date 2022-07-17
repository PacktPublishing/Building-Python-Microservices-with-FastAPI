from fastapi import APIRouter
from services.tasks import addTask, multiply_callback
from celery import chain, group, chord
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
router = APIRouter()


@router.get("/tasks1")
async def index():
    
    result = addTask.apply_async(kwargs={'x':10, 'y':20,}, task_id="add-task1").get()
    return {'message' : result }

@router.get("/tasks2")
async def index2():
    
    result = chain(addTask.s(10, 20).set(queue='default'), addTask.s(20).set(queue='default'), addTask.s(30).set(queue='default')).apply_async()
    return {'message' : result.get(timeout = 10) }

@router.get("/tasks3")
async def index3():
    result = group([addTask.s(10, 20).set(queue='default'), addTask.s(10, 20).set(queue='default'), addTask.s(20, 30).set(queue='default')]).apply_async()
    return {'message' : result.get(timeout = 10) }

@router.get("/tasks4")
async def index4():
    result = chord([addTask.s(10, 20).set(queue='default'), addTask.s(10, 20).set(queue='default'), addTask.s(20, 30).set(queue='default')])(multiply_callback.s().set(queue='default'))
    return {'message' : result.get(timeout = 10) }

@router.get("/tasks5")
async def index5():
    result = group(addTask.starmap([(10, 20), (20, 40), (10, 10)]).set(queue='default')).apply_async()
    return {'message' : result.get(timeout = 10) }

