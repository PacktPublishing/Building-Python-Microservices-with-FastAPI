from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from library_mgt.models.data.library import BookIssuance, BookRequest
from library_mgt.models.request.library import BookIssuanceReq, BookRequestReq, BookReturnReq
from library_mgt.services.issuance import BookIssuanceService
from library_mgt.services.reservations import BookRequestService

from uuid import uuid4
router = APIRouter()

@router.post('/book/request')
def request_book(request:BookRequestReq): 
    book_request = BookRequest(status=request.status, request_date=request.book_id, book_id=request.book_id, req_id=uuid4().int) 
    request_service = BookRequestService()
    result = request_service.add_book_request(book_request)
    if result: 
        return jsonable_encoder(book_request)
    else: 
        return JSONResponse(content={'message': 'book request not successful'}, status_code=500)

@router.post('/book/request/list')
def list_requests(): 
    request_service = BookRequestService()
    return request_service.list_book_request()

@router.post('/book/issuance')
def approve_request(approval:BookIssuanceReq): 
    book_approval = BookIssuance(approved_by=approval.approved_by, approved_date=approval.approved_date, req_id=approval.req_id, issue_id=uuid4().int)
    approval_service = BookIssuanceService()
    result = approval_service.add_book_release(book_approval)
    if result: 
        return jsonable_encoder(book_approval)
    else: 
        return JSONResponse(content={'message': 'book issuance not successful'}, status_code=500)

@router.get('/book/issuance/list')
def list_issuances(): 
    approval_service = BookIssuanceService()
    return approval_service.list_book_release()

@router.post('/book/issuance/return')
def return_issued_book(returning:BookReturnReq): 
    approval_service:BookIssuanceService = BookIssuanceService()
    result = approval_service.return_issued_book(returning.issue_id, returning.returned_date)
    if result: 
        return jsonable_encoder(returning)
    else: 
        return JSONResponse(content={'message': 'book issuance not successful'}, status_code=500)