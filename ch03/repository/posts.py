from datetime import date, datetime
from model.classifications import RecipeRating
from model.posts import Post
from uuid import uuid1 

posts = dict()

class PostRepository: 
    def __init__(self): 
        pass
        
    def insert_post(self, post: Post): 
        posts[post.id] = post
        
    def query_posts(self): 
        return list(posts.values())