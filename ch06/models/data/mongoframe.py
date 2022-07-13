from mongoframes import Frame, SubFrame

class Book(Frame):
    _fields = {
        'id ',
        'isbn',
        'author', 
        'date_published', 
        'title', 
        'edition',
        'price',
        'category'
    }
    _collection = "book"
    
    
class Category(SubFrame):
    
    _fields = {
        'id',
        'name',
        'description',
        'date_added'
        }
    
    _collection = "category"

class Reference(Frame):

    _fields = {
        'id',
        'name',
        'description',
        'categories'
        }
    
    _collection = "reference"