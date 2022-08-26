from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.requests.members import ProfileMembersReq
from repository.pony.members import MemberRepository, MemberGymClassRepository
router = APIRouter()


@router.post("/member/add")
def add_member(req:ProfileMembersReq): 
    repo = MemberRepository()
    mem_profile = dict()
    mem_profile["id"] = req.id
    mem_profile["firstname"] = req.firstname
    mem_profile["lastname"] = req.lastname
    mem_profile["age"] = req.age
    mem_profile["height"] = req.height
    mem_profile["weight"] = req.weight
    mem_profile["membership_type"] = req.membership_type
    mem_profile["trainer_id"] = req.trainer_id
    
    result = repo.insert_member(mem_profile)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create profile encountered'}, status_code=500)

@router.patch("/member/update")
def update_member(id:int, req:ProfileMembersReq): 
    mem_profile_dict = req.dict(exclude_unset=True)
    repo = MemberRepository()
    result = repo.update_member(id, mem_profile_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update profile problem encountered'}, status_code=500)
    
@router.delete("/member/delete/{id}")
def delete_member(id:int): 
    repo = MemberRepository()
    result = repo.delete_member(id)
    if result == True: 
        return JSONResponse(content={'message':'update profile successful'}, status_code=201) 
    else: 
        return JSONResponse(content={'message':'update profile problem encountered'}, status_code=500)
    
@router.get("/member/list")
def list_members():
    repo = MemberRepository()
    return repo.get_all_member()

@router.get("/member/get/{id}")
def get_member(id:int):
    repo = MemberRepository()
    return repo.get_member(id)

@router.get("/member/classes/list")
def list_members_class(): 
    repo = MemberGymClassRepository()
    return repo.join_member_class()
