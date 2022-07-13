from datetime import date, datetime
from model.classifications import RecipeRating
from model.posts import Post
from uuid import uuid1 

posts = dict()

class PostRepository: 
    def __init__(self): 
        post1 = Post(id=uuid1(), feedback="Delicious", rating=RecipeRating.five, userId=uuid1(), date_posted='2020-10-10')
        posts[post1.id] = post1
        
    def insert_post(self, post: Post): 
        posts[post.id] = post
        
    def query_posts(self): 
        return posts.values();