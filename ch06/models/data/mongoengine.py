from mongoengine import Document, BooleanField, StringField, IntField, FloatField, DateField, SequenceField, EmbeddedDocument, EmbeddedDocumentField, EmbeddedDocumentListField
import json 

class BookForSale(EmbeddedDocument): 
    id = SequenceField(required=True, primary_key=True)
    isbn = StringField(db_field="isbn", max_length=50, required=True)
    author = StringField(db_field="author", max_length=50, required=True)
    date_published = DateField(db_field="date_published", required=True)
    title = StringField(db_field="title", max_length=100, required=True)
    edition = IntField(db_field="edition", required=True)
    price = FloatField(db_field="price", required=True)
    
    def to_json(self):
            return {
            "id": self.id,
            "isbn": self.isbn,
            "author": self.author,
            "date_published": self.date_published.strftime("%m/%d/%Y"),
            "title": self.title,
            "edition": self.edition,
            "price": self.price
        }
        
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

class UserProfile(EmbeddedDocument):
   firstname = StringField(db_field="firstname", max_length=50, required=True)
   lastname = StringField(db_field="lastname", max_length=50, required=True)
   middlename = StringField(db_field="middlename", max_length=50, required=True)
   position = StringField(db_field="position", max_length=50, required=True)
   date_approved = DateField(db_field="date_approved", required=True)
   status = BooleanField(db_field="status", required=True)
   level = IntField(db_field="level", required=True)
   login_id = IntField(db_field="login_id", required=True)
   booksale = EmbeddedDocumentListField(BookForSale, required=False)
   
   def to_json(self):
            return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "middlename": self.middlename,
            "position": self.position,
            "date_approved": self.date_approved.strftime("%m/%d/%Y"),
            "status": self.status,
            "level": self.level,
            "login_id": self.login_id,
            "booksale": self.booksale
        }
        
   @classmethod
   def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

class Login(Document): 
    id = SequenceField(required=True, primary_key=True)
    username = StringField(db_field="username", max_length=50, required=True, unique=True)
    password = StringField(db_field="password", max_length=50, required=True)
    profile = EmbeddedDocumentField(UserProfile, required=False)
    
    def to_json(self):
            return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "profile": self.profile
        }
        
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

