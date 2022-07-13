from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from library_mgt.models.data.library import Book
from library_mgt.models.request.library import BookReq, BookDetails
from library_mgt.services.books import BookService

router = APIRouter()


# add books
@router.post('/book/add')
def add_books(book:BookReq):
    book = Book(classification=book.classification, year_published=book.year_published, edition=book.edition, author=book.author, title=book.title, book_id=book.book_id)
    book_service = BookService()
    result = book_service.add_book(book)
    if result == True: 
        return jsonable_encoder(book)
    else: 
        return JSONResponse(content={'message': 'book insertion not successful'}, status_code=500)

# view books
@router.get('/book/list')
def view_books(): 
    book_service = BookService()
    return book_service.list_book()

# delete book
@router.delete('/book/list')
def delete_book(book_id:int): 
    book_service = BookService()
    result = book_service.remove_book(book_id)
    if result == True: 
        return JSONResponse(content={'message': 'book insertion successful'}, status_code=201)
    else: 
        return JSONResponse(content={'message': 'book insertion not successful'}, status_code=500)

# update book info
@router.patch('/book/update')
def update_book_details(book_id:int, book_details:BookDetails): 
    book_dict = book_details.dict(exclude_unset=True)
    book_service = BookService()
    result = book_service.update_book(book_id, book_dict )
    if result: 
        return JSONResponse(content={'message':'book details updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'book details update error'}, status_code=500)
