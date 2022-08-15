
from uuid import UUID
from repository.recipes import recipes
recipe_bad = dict()

class BadRecipeRepository: 
    def __init__(self): 
        pass
    
    def add_bad_recipe(self, id:UUID): 
        recipe_bad[id] = id
       
        
    def query_bad_recipes(self): 
        return list(recipe_bad.values())