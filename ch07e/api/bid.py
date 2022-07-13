from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Bids, Login
from repository.bids import BidsRepository
from models.request.bids import BidsReq
from db_config.sqlalchemy_connect import sess_db
from security.secure import get_current_valid_user

router = APIRouter()

@router.post("/bid/add")
def add_bid(req: BidsReq, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write"]), sess:Session = Depends(sess_db)): 
    bid_dict = req.dict(exclude_unset=True)
    repo:BidsRepository = BidsRepository(sess)
    bid = Bids(**bid_dict)
    result = repo.insert_bid(bid)
    if result == True:
        return bid
    else: 
        return JSONResponse(content={'message':'create bid problem encountered'}, status_code=500)   

@router.patch("/bid/update")
def update_bid(id:int, req: BidsReq, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write"]),  sess:Session = Depends(sess_db)): 
    bid_dict = req.dict(exclude_unset=True)
    repo:BidsRepository = BidsRepository(sess)
    result = repo.update_bid(id, bid_dict )
    if result: 
        return JSONResponse(content={'message':'bid updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update bid error'}, status_code=500)


@router.delete("/bid/delete/{id}")
def delete_bid(id:int, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write"]),  sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    result = repo.delete_bid(id )
    if result: 
        return JSONResponse(content={'message':'auction updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update auction error'}, status_code=500)

@router.get("/bid/all")
def list_all_bid(current_user: Login = Security(get_current_valid_user, scopes=["bidder_read"]),  sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    result = repo.get_all_bids()
    return result  

@router.post("/bid/{id}")
def get_bid(id:int, current_user: Login = Security(get_current_valid_user, scopes=["bidder_read"]), sess:Session = Depends(sess_db)): 
    repo:BidsRepository = BidsRepository(sess)
    result = repo.get_bid(id)
    return result  
