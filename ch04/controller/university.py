from fastapi import APIRouter

router = APIRouter()

@router.get("/university/{portal_id}")
def access_portal(portal_id:int): 
    return {'message': 'University ERP Systems'}

 