from fastapi import Depends
from model.recipes import Recipe
from repository.factory import get_recipe_repo


class RecipeService: 
     
    def __init__(self, repo=Depends(get_recipe_repo)):
        self.repo = repo
        
    def get_recipes(self):
        return self.repo.query_recipes()
    
    def add_recipe(self, recipe: Recipe):
        self.repo.insert_recipe(recipe)
        
    