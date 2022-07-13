from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from faculty_mgt.models.request.library import BookRequestReq, BookReturnReq
from json import dumps
import requests

router = APIRouter()

@router.get('/books/access/list')
def list_all_books(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/ch04/library/book/list')
        return response.json()

@router.get('/books/request/list')
def list_all_request(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/ch04/library/book/request/list',)
        return response.json()

@router.post('/books/request/borrow')
def request_borrow_book(request:BookRequestReq): 
    with requests.Session() as sess:
        response = sess.post('http://localhost:8000/ch04/library/book/request', data=dumps(jsonable_encoder(request)))
        return response.content

@router.get('/books/issuance/list')
def list_all_issuance(): 
    with requests.Session() as sess:
        response = sess.get('http://localhost:8000/ch04/library/book/issuance/list')
        return response.json()

@router.post('/books/returning')
def return_book(returning: BookReturnReq): 
    with requests.Session() as sess:
        response = sess.post('http://localhost:8000/ch04/library/book/issuance/return', data=dumps(jsonable_encoder(returning)))
        return response.json()


