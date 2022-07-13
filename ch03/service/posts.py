from fastapi import Depends
from model.posts import Post
from repository.factory import get_post_repo

class PostService: 
    
    def __init__(self, repo=Depends(get_post_repo)): 
        self.repo = repo
        
    def add_post(self, post: Post): 
        self.repo.insert_post(post)
        
    def get_posts(self): 
        return self.repo.query_posts()