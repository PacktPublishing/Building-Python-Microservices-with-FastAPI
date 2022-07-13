from typing import Dict, Any
from models.data.mongoengine import Book, Category

class BookRepository: 
    def insert_book(self, details:Dict[str, Any]) -> bool: 
        try:
            book = Book(**details)
            book.save()
        except Exception as e:
            print(e)
            return False 
        return True
    
    def add_category(self, id:int, details:Dict[str, Any]) -> bool: 
        try:
            category = Category(**details)
            book = Book.objects(id=id).get()
            book.update(category=category)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def delete_category(self, id:int) -> bool: 
        try:
            book = Book.objects(id=id).get()
            book.update(category=None)
        except Exception as e:
            print(e)
            return False 
        return True
    
    def update_book(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          book = Book.objects(id=id).get()
          book.update(**details)
       except: 
           return False 
       return True
   
    def delete_book(self, id:int) -> bool: 
        try:
            book = Book.objects(id=id).get()
            book.update(unset__profile=1)
        except: 
            return False 
        return True
    
        
    def get_all_book(self):
        books = Book.objects()
        return books
    
    def get_book(self, id:int): 
        book = Book.objects(id=id).get()
        return book