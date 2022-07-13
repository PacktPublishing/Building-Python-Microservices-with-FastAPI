from typing import Dict

from library_mgt.models.data.library import Book, BookRequest, BookIssuance

book_tbl:Dict[int, Book] = dict()
book_request_tbl:Dict[int, BookRequest] = dict()
book_issuance_tbl:Dict[int, BookIssuance] = dict()

