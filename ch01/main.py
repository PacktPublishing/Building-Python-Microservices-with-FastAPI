from enum import Enum
from typing import Optional, List, Dict
from uuid import UUID, uuid1

from fastapi import FastAPI, Form, Cookie, Header, Response
from pydantic import BaseModel

from bcrypt import hashpw, gensalt, checkpw
from datetime import date, datetime

from string import ascii_lowercase
from random import random


app = FastAPI()

valid_users = dict()
valid_profiles = dict()
pending_users = dict()
discussion_posts = dict()
request_headers = dict()
cookies = dict()

   
class User(BaseModel):
    username: str
    password: str

class ValidUser(BaseModel):
    id: UUID
    username: str
    password: str
    passphrase: str

class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"
    
class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType
  
class PostType(str, Enum):
    information = "information" 
    inquiry = "inquiry"
    quote = "quote"
    twit = "twit"
    
class Post(BaseModel):
    topic: Optional[str] = None
    message: str
    date_posted: datetime
    
class ForumPost(BaseModel):
    id: UUID
    topic: Optional[str] = None
    message: str
    post_type: PostType
    date_posted: datetime
    username: str

class ForumDiscussion(BaseModel):
    id: UUID
    main_post: ForumPost
    replies: Optional[List[ForumPost]] = None
    author: UserProfile

# first sample API
@app.get("/ch01/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}
    
@app.post("/ch01/login/signup")
def signup(uname: str, passwd: str):
    if ( uname == None and passwd == None):
        return {"message" : "invalid user"}
    elif not valid_users.get(uname) == None:
        return {"message": "user exists"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname] = user
        return user

@app.post("/ch01/list/users/pending")
def list_pending_users():
    return pending_users

@app.delete("/ch01/delete/users/pending")
def delete_pending_users(accounts: List[str] = []):
    for user in accounts:
        del pending_users[user]
    return {"message": "deleted pending users"}


@app.post("/ch01/login/validate", response_model=ValidUser)
def approve_user(user: User):
    
    if not valid_users.get(user.username) == None:
        return ValidUser(id=None, username = None, password = None, passphrase = None)
    else:
        valid_user = ValidUser(id=uuid1(), username= user.username, password  = user.password, passphrase = hashpw(user.password.encode(),gensalt()))
        valid_users[user.username] = valid_user
        del pending_users[user.username]
        return valid_user
    
@app.delete("/ch01/login/remove/all")
def delete_users(usernames: List[str]):
    for user in usernames:
        del valid_users[user]
    return {"message": "deleted users"}

@app.delete("/ch01/login/remove/{username}")
def delete_user(username: str):
    if username == None:
        return {"message": "invalid user"}
    else:
        del valid_users[username]
        return {"message": "deleted user"}


@app.get("/ch01/list/users/valid")
def list_valid_users():
    return valid_users

@app.get("/ch01/login/")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.passphrase.encode()):
            return user
        else:
            return {"message": "invalid user"}

# should be above /ch01/login/{username}/{password}
@app.get("/ch01/login/details/info")
def login_info():
    return {"message": "username and password are needed"}

# should be above /ch01/login/{username}/{password}
@app.get("/ch01/login/password/change")
def change_password(username: str, old_passw: str = '', new_passw: str = ''):
    passwd_len = 8
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif old_passw == '' or new_passw == '':
        characters = ascii_lowercase
        temporary_passwd = ''.join(random.choice(characters) for i in range(passwd_len))
        user = valid_users.get(username)
        user.password = temporary_passwd
        user.passphrase = hashpw(temporary_passwd.encode(),gensalt())
        return user
    else:
        user = valid_users.get(username)
        if user.password == old_passw:
            user.password = new_passw
            user.passphrase = hashpw(new_passw.encode(),gensalt())
            return user
        else:
            return {"message": "invalid user"}

# should be above /ch01/login/{username}/{password}
@app.post("/ch01/login/username/unlock")
def unlock_username(id: Optional[UUID] = None):
    if id == None:
        return {"message": "token needed"}
    else:
        for key, val in valid_users.items():
            if val.id == id:
                return {"username": val.username}
        return {"message": "user does not exist"}

# should be above /ch01/login/{username}/{password}
@app.post("/ch01/login/password/unlock")
def unlock_password(username: Optional[str] = None, id: Optional[UUID] = None ):
    if username == None:
        return {"message": "username is required"}
    elif valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        if id == None:
            return {"message": "token needed"}
        else:
            user = valid_users.get(username)
            if user.id == id:
                return {"password": user.password}
            else:
                return {"message": "invalid token"}
            
@app.get("/ch01/login/{username}/{password}")
def login_with_token(username: str, password:str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users[username]
        if user.id == id and checkpw(password.encode(), user.passphrase):
            return user
        else:
            return {"message": "invalid user"}



        
@app.post("/ch01/account/profile/add", response_model=UserProfile)
def add_profile(uname: str, 
                fname: str = Form(...), 
                lname: str = Form(...),
                mid_init: str = Form(...),
                user_age: int = Form(...),
                sal: float = Form(...),
                bday: str = Form(...),
                utype: UserType = Form(...)):
    if valid_users.get(uname) == None:
        return UserProfile(firstname=None, lastname=None, middle_initial=None, age=None, birthday=None, salary=None, user_type=None)
    else:
        profile = UserProfile(firstname=fname, lastname=lname, middle_initial=mid_init, age=user_age, birthday=datetime.strptime(bday, '%m/%d/%Y'), salary=sal, user_type=utype)
        valid_profiles[uname] = profile
        return profile

@app.put("/ch01/account/profile/update/{username}")
def update_profile(username: str, id: UUID, new_profile: UserProfile):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            valid_profiles[username] = new_profile
            return {"message": "successfully updated"}
        else:
            return {"message": "user does not exist"}

@app.patch("/ch01/account/profile/update/names/{username}")
def update_profile_names(id: UUID, username: str = '' , new_names: Optional[Dict[str, str]] = None):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif new_names == None:
        return {"message": "new names are required"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            profile = valid_profiles[username]
            profile.firstname = new_names['fname']
            profile.lastname = new_names['lname']
            profile.middle_initial = new_names['mi']
            valid_profiles[username] = profile
            return {"message": "successfully updated"}
        else:
            return {"message": "user does not exist"}

@app.get("/ch01/account/profile/view/{username}")
def access_profile(username: str, id: UUID):
    if valid_users.get(username) == None:
            return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            return valid_profiles[username]
        else:
            return {"message": "user does not exist"}

        
@app.post("/ch01/discussion/posts/add/{username}")
def post_discussion(username: str, post: Post, post_type: PostType):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif not (discussion_posts.get(id) == None):
            return {"message": "post already exists"}
    else:
        forum_post = ForumPost(id=uuid1(), topic=post.topic, message=post.message, post_type=post_type, date_posted=post.date_posted, username=username)
        user = valid_profiles[username]
        forum = ForumDiscussion(id=uuid1(), main_post=forum_post, author=user, replies=list())
        discussion_posts[forum.id] = forum
        return forum

@app.post("/ch01/discussion/posts/reply/{username}")
def post_reply(username: str, id: UUID, post_type: PostType, post_reply: Post):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        reply = ForumPost(id=uuid1(), topic=post_reply.topic, message=post_reply.message, post_type=post_type, date_posted=post_reply.date_posted, username=username)
        main_post = discussion_posts[id]
        main_post.replies.append(reply)
        return reply

@app.put("/ch01/discussion/posts/update/{username}")
def update_discussion(username: str, id: UUID, post_type: PostType, post: Post):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        forum_post = ForumPost(id=uuid1(), topic=post.topic, message=post.message, post_type=post_type, date_posted=post.date_posted, username=username)
        forum = discussion_posts[id] 
        forum.main_post = forum_post
        return {"message": "main post update"}

@app.delete("/ch01/discussion/posts/remove/{username}")
def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        del discussion_posts[id] 
        return {"message": "main post deleted"}
    
@app.get("/ch01/discussion/posts/view/{username}")
def view_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        forum = discussion_posts[id]
        return forum
    
@app.get("/ch01/headers/verify")
def verify_headers(host: Optional[str] = Header(None), 
                   accept: Optional[str] = Header(None),
                   accept_language: Optional[str] = Header(None),
                   accept_encoding: Optional[str] = Header(None),
                   user_agent: Optional[str] = Header(None)):
    request_headers["Host"] = host
    request_headers["Accept"] = accept
    request_headers["Accept-Language"] = accept_language
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["User-Agent"] = user_agent
    return request_headers
    

@app.get("/ch01/login/cookies")
def access_cookie(userkey: Optional[str] = Cookie(None), identity: Optional[str] = Cookie(None)):
    cookies["userkey"] = userkey
    cookies["identity"] = identity
    return cookies

@app.post("/ch01/login/rememberme/create/")
def create_cookies(resp: Response, id: UUID, username: str = ''):
    resp.set_cookie(key="userkey", value=username)
    resp.set_cookie(key="identity", value=str(id))
    return {"message": "remember-me tokens created"}

    