from repository.recipes import recipes
from uuid import UUID

def get_recipe_names(): 
    recipes_list = [val.name for val in recipes.values()]
    return recipes_list

def get_recipe_ingredients(rid: UUID): 
    ingredients = recipes[rid].ingredients
    return ingredients